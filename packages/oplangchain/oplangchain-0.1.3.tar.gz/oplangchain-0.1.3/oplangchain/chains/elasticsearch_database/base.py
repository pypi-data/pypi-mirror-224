"""Chain for interacting with Elasticsearch Database."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional

from pydantic import Extra, root_validator

from oplangchain.callbacks.manager import CallbackManagerForChainRun
from oplangchain.chains.base import Chain
from oplangchain.chains.elasticsearch_database.prompts import ANSWER_PROMPT, DSL_PROMPT
from oplangchain.chains.llm import LLMChain
from oplangchain.output_parsers.json import SimpleJsonOutputParser
from oplangchain.schema import BaseLLMOutputParser, BasePromptTemplate
from oplangchain.schema.language_model import BaseLanguageModel

if TYPE_CHECKING:
    from elasticsearch import Elasticsearch

INTERMEDIATE_STEPS_KEY = "intermediate_steps"


class ElasticsearchDatabaseChain(Chain):
    """Chain for interacting with Elasticsearch Database.

    Example:
        .. code-block:: python

            from oplangchain import ElasticsearchDatabaseChain, OpenAI
            from elasticsearch import Elasticsearch

            database = Elasticsearch("http://localhost:9200")
            db_chain = ElasticsearchDatabaseChain.from_llm(OpenAI(), database)
    """

    query_chain: LLMChain
    """Chain for creating the ES query."""
    answer_chain: LLMChain
    """Chain for answering the user question."""
    database: Any
    """Elasticsearch database to connect to of type elasticsearch.Elasticsearch."""
    top_k: int = 10
    """Number of results to return from the query"""
    ignore_indices: Optional[List[str]] = None
    include_indices: Optional[List[str]] = None
    input_key: str = "question"  #: :meta private:
    output_key: str = "result"  #: :meta private:
    sample_documents_in_index_info: int = 3
    return_intermediate_steps: bool = False
    """Whether or not to return the intermediate steps along with the final answer."""

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid
        arbitrary_types_allowed = True

    @root_validator()
    def validate_indices(cls, values: dict) -> dict:
        if values["include_indices"] and values["ignore_indices"]:
            raise ValueError(
                "Cannot specify both 'include_indices' and 'ignore_indices'."
            )
        return values

    @property
    def input_keys(self) -> List[str]:
        """Return the singular input key.

        :meta private:
        """
        return [self.input_key]

    @property
    def output_keys(self) -> List[str]:
        """Return the singular output key.

        :meta private:
        """
        if not self.return_intermediate_steps:
            return [self.output_key]
        else:
            return [self.output_key, INTERMEDIATE_STEPS_KEY]

    def _list_indices(self) -> List[str]:
        all_indices = [
            index["index"] for index in self.database.cat.indices(format="json")
        ]

        if self.include_indices:
            all_indices = [i for i in all_indices if i in self.include_indices]
        if self.ignore_indices:
            all_indices = [i for i in all_indices if i not in self.ignore_indices]

        return all_indices

    def _get_indices_infos(self, indices: List[str]) -> str:
        mappings = self.database.indices.get_mapping(index=",".join(indices))
        if self.sample_documents_in_index_info > 0:
            for k, v in mappings.items():
                hits = self.database.search(
                    index=k,
                    query={"match_all": {}},
                    size=self.sample_documents_in_index_info,
                )["hits"]["hits"]
                hits = [str(hit["_source"]) for hit in hits]
                mappings[k]["mappings"] = str(v) + "\n\n/*\n" + "\n".join(hits) + "\n*/"
        return "\n\n".join(
            [
                "Mapping for index {}:\n{}".format(index, mappings[index]["mappings"])
                for index in mappings
            ]
        )

    def _search(self, indices: List[str], query: str) -> str:
        result = self.database.search(index=",".join(indices), body=query)
        return str(result)

    def _call(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        input_text = f"{inputs[self.input_key]}\nESQuery:"
        _run_manager.on_text(input_text, verbose=self.verbose)
        indices = self._list_indices()
        indices_info = self._get_indices_infos(indices)
        query_inputs: dict = {
            "input": input_text,
            "top_k": str(self.top_k),
            "indices_info": indices_info,
            "stop": ["\nESResult:"],
        }
        intermediate_steps: List = []
        try:
            intermediate_steps.append(query_inputs)  # input: es generation
            es_cmd = self.query_chain.run(
                callbacks=_run_manager.get_child(),
                **query_inputs,
            )

            _run_manager.on_text(es_cmd, color="green", verbose=self.verbose)
            intermediate_steps.append(
                es_cmd
            )  # output: elasticsearch dsl generation (no checker)
            intermediate_steps.append({"es_cmd": es_cmd})  # input: ES search
            result = self._search(indices=indices, query=es_cmd)
            intermediate_steps.append(str(result))  # output: ES search

            _run_manager.on_text("\nESResult: ", verbose=self.verbose)
            _run_manager.on_text(result, color="yellow", verbose=self.verbose)

            _run_manager.on_text("\nAnswer:", verbose=self.verbose)
            answer_inputs: dict = {"data": result, "input": input_text}
            intermediate_steps.append(answer_inputs)  # input: final answer
            final_result = self.answer_chain.run(
                callbacks=_run_manager.get_child(),
                **answer_inputs,
            )

            intermediate_steps.append(final_result)  # output: final answer
            _run_manager.on_text(final_result, color="green", verbose=self.verbose)
            chain_result: Dict[str, Any] = {self.output_key: final_result}
            if self.return_intermediate_steps:
                chain_result[INTERMEDIATE_STEPS_KEY] = intermediate_steps
            return chain_result
        except Exception as exc:
            # Append intermediate steps to exception, to aid in logging and later
            # improvement of few shot prompt seeds
            exc.intermediate_steps = intermediate_steps  # type: ignore
            raise exc

    @property
    def _chain_type(self) -> str:
        return "elasticsearch_database_chain"

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        database: Elasticsearch,
        *,
        query_prompt: Optional[BasePromptTemplate] = None,
        answer_prompt: Optional[BasePromptTemplate] = None,
        query_output_parser: Optional[BaseLLMOutputParser] = None,
        **kwargs: Any,
    ) -> ElasticsearchDatabaseChain:
        """Convenience method to construct ElasticsearchDatabaseChain from an LLM.

        Args:
            llm: The language model to use.
            database: The Elasticsearch db.
            query_prompt: The prompt to use for query construction.
            answer_prompt: The prompt to use for answering user question given data.
            query_output_parser: The output parser to use for parsing model-generated
                ES query. Defaults to SimpleJsonOutputParser.
            **kwargs: Additional arguments to pass to the constructor.
        """
        query_prompt = query_prompt or DSL_PROMPT
        query_output_parser = query_output_parser or SimpleJsonOutputParser()
        query_chain = LLMChain(
            llm=llm, prompt=query_prompt, output_parser=query_output_parser
        )
        answer_prompt = answer_prompt or ANSWER_PROMPT
        answer_chain = LLMChain(llm=llm, prompt=answer_prompt)
        return cls(
            query_chain=query_chain,
            answer_chain=answer_chain,
            database=database,
            **kwargs,
        )
