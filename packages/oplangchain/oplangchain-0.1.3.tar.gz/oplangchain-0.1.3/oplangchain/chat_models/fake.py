"""Fake ChatModel for testing purposes."""
from typing import Any, Dict, List, Optional

from oplangchain.callbacks.manager import CallbackManagerForLLMRun
from oplangchain.chat_models.base import SimpleChatModel
from oplangchain.schema.messages import BaseMessage


class FakeListChatModel(SimpleChatModel):
    """Fake ChatModel for testing purposes."""

    responses: List
    i: int = 0

    @property
    def _llm_type(self) -> str:
        return "fake-list-chat-model"

    def _call(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """First try to lookup in queries, else return 'foo' or 'bar'."""
        response = self.responses[self.i]
        if self.i < len(self.responses) - 1:
            self.i += 1
        else:
            self.i = 0
        return response

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {"responses": self.responses}
