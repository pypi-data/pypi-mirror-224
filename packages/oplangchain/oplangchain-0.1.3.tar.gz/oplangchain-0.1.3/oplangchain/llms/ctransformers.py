from functools import partial
from typing import Any, Dict, List, Optional, Sequence

from pydantic import root_validator

from oplangchain.callbacks.manager import (
    AsyncCallbackManagerForLLMRun,
    CallbackManagerForLLMRun,
)
from oplangchain.llms.base import LLM


class CTransformers(LLM):
    """C Transformers LLM models.

    To use, you should have the ``ctransformers`` python package installed.
    See https://github.com/marella/ctransformers

    Example:
        .. code-block:: python

            from oplangchain.llms import CTransformers

            llm = CTransformers(model="/path/to/ggml-gpt-2.bin", model_type="gpt2")
    """

    client: Any  #: :meta private:

    model: str
    """The path to a model file or directory or the name of a Hugging Face Hub
    model repo."""

    model_type: Optional[str] = None
    """The model type."""

    model_file: Optional[str] = None
    """The name of the model file in repo or directory."""

    config: Optional[Dict[str, Any]] = None
    """The config parameters.
    See https://github.com/marella/ctransformers#config"""

    lib: Optional[str] = None
    """The path to a shared library or one of `avx2`, `avx`, `basic`."""

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Get the identifying parameters."""
        return {
            "model": self.model,
            "model_type": self.model_type,
            "model_file": self.model_file,
            "config": self.config,
        }

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "ctransformers"

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that ``ctransformers`` package is installed."""
        try:
            from ctransformers import AutoModelForCausalLM
        except ImportError:
            raise ImportError(
                "Could not import `ctransformers` package. "
                "Please install it with `pip install ctransformers`"
            )

        config = values["config"] or {}
        values["client"] = AutoModelForCausalLM.from_pretrained(
            values["model"],
            model_type=values["model_type"],
            model_file=values["model_file"],
            lib=values["lib"],
            **config,
        )
        return values

    def _call(
        self,
        prompt: str,
        stop: Optional[Sequence[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Generate text from a prompt.

        Args:
            prompt: The prompt to generate text from.
            stop: A list of sequences to stop generation when encountered.

        Returns:
            The generated text.

        Example:
            .. code-block:: python

                response = llm("Tell me a joke.")
        """
        text = []
        _run_manager = run_manager or CallbackManagerForLLMRun.get_noop_manager()
        for chunk in self.client(prompt, stop=stop, stream=True):
            text.append(chunk)
            _run_manager.on_llm_new_token(chunk, verbose=self.verbose)
        return "".join(text)

    async def _acall(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Asynchronous Call out to CTransformers generate method.
        Very helpful when streaming (like with websockets!)

        Args:
            prompt: The prompt to pass into the model.
            stop: A list of strings to stop generation when encountered.

        Returns:
            The string generated by the model.

        Example:
            .. code-block:: python
                response = llm("Once upon a time, ")
        """
        text_callback = None
        if run_manager:
            text_callback = partial(run_manager.on_llm_new_token, verbose=self.verbose)

        text = ""
        for token in self.client(prompt, stop=stop, stream=True):
            if text_callback:
                await text_callback(token)
            text += token

        return text
