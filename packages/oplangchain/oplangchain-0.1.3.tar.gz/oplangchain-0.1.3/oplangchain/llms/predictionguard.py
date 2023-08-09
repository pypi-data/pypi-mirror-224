import logging
from typing import Any, Dict, List, Optional

from pydantic import Extra, root_validator

from oplangchain.callbacks.manager import CallbackManagerForLLMRun
from oplangchain.llms.base import LLM
from oplangchain.llms.utils import enforce_stop_tokens
from oplangchain.utils import get_from_dict_or_env

logger = logging.getLogger(__name__)


class PredictionGuard(LLM):
    """Prediction Guard large language models.

    To use, you should have the ``predictionguard`` python package installed, and the
    environment variable ``PREDICTIONGUARD_TOKEN`` set with your access token, or pass
    it as a named parameter to the constructor. To use Prediction Guard's API along
    with OpenAI models, set the environment variable ``OPENAI_API_KEY`` with your
    OpenAI API key as well.

    Example:
        .. code-block:: python

            pgllm = PredictionGuard(model="MPT-7B-Instruct",
                                    token="my-access-token",
                                    output={
                                        "type": "boolean"
                                    })
    """

    client: Any  #: :meta private:
    model: Optional[str] = "MPT-7B-Instruct"
    """Model name to use."""

    output: Optional[Dict[str, Any]] = None
    """The output type or structure for controlling the LLM output."""

    max_tokens: int = 256
    """Denotes the number of tokens to predict per generation."""

    temperature: float = 0.75
    """A non-negative float that tunes the degree of randomness in generation."""

    token: Optional[str] = None
    """Your Prediction Guard access token."""

    stop: Optional[List[str]] = None

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that the access token and python package exists in environment."""
        token = get_from_dict_or_env(values, "token", "PREDICTIONGUARD_TOKEN")
        try:
            import predictionguard as pg

            values["client"] = pg.Client(token=token)
        except ImportError:
            raise ImportError(
                "Could not import predictionguard python package. "
                "Please install it with `pip install predictionguard`."
            )
        return values

    @property
    def _default_params(self) -> Dict[str, Any]:
        """Get the default parameters for calling the Prediction Guard API."""
        return {
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
        }

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Get the identifying parameters."""
        return {**{"model": self.model}, **self._default_params}

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "predictionguard"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Call out to Prediction Guard's model API.
        Args:
            prompt: The prompt to pass into the model.
        Returns:
            The string generated by the model.
        Example:
            .. code-block:: python
                response = pgllm("Tell me a joke.")
        """
        import predictionguard as pg

        params = self._default_params
        if self.stop is not None and stop is not None:
            raise ValueError("`stop` found in both the input and default params.")
        elif self.stop is not None:
            params["stop_sequences"] = self.stop
        else:
            params["stop_sequences"] = stop

        response = pg.Completion.create(
            model=self.model,
            prompt=prompt,
            output=self.output,
            temperature=params["temperature"],
            max_tokens=params["max_tokens"],
            **kwargs,
        )
        text = response["choices"][0]["text"]

        # If stop tokens are provided, Prediction Guard's endpoint returns them.
        # In order to make this consistent with other endpoints, we strip them.
        if stop is not None or self.stop is not None:
            text = enforce_stop_tokens(text, params["stop_sequences"])

        return text
