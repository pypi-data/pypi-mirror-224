"""Chain that runs an arbitrary python function."""
import functools
import logging
from typing import Any, Awaitable, Callable, Dict, List, Optional

from oplangchain.callbacks.manager import (
    AsyncCallbackManagerForChainRun,
    CallbackManagerForChainRun,
)
from oplangchain.chains.base import Chain

logger = logging.getLogger(__name__)


class TransformChain(Chain):
    """Chain that transforms the chain output.

    Example:
        .. code-block:: python

            from oplangchain import TransformChain
            transform_chain = TransformChain(input_variables=["text"],
             output_variables["entities"], transform=func())
    """

    input_variables: List[str]
    """The keys expected by the transform's input dictionary."""
    output_variables: List[str]
    """The keys returned by the transform's output dictionary."""
    transform: Callable[[Dict[str, str]], Dict[str, str]]
    """The transform function."""
    atransform: Optional[Callable[[Dict[str, Any]], Awaitable[Dict[str, Any]]]] = None
    """The async coroutine transform function."""

    @staticmethod
    @functools.lru_cache
    def _log_once(msg: str) -> None:
        """Log a message once.

        :meta private:
        """
        logger.warning(msg)

    @property
    def input_keys(self) -> List[str]:
        """Expect input keys.

        :meta private:
        """
        return self.input_variables

    @property
    def output_keys(self) -> List[str]:
        """Return output keys.

        :meta private:
        """
        return self.output_variables

    def _call(
        self,
        inputs: Dict[str, str],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, str]:
        return self.transform(inputs)

    async def _acall(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[AsyncCallbackManagerForChainRun] = None,
    ) -> Dict[str, Any]:
        if self.atransform is not None:
            return await self.atransform(inputs)
        else:
            self._log_once(
                "TransformChain's atransform is not provided, falling"
                " back to synchronous transform"
            )
            return self.transform(inputs)
