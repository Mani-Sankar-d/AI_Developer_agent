from AI_Developer_agent.backend.app.llm.models import LLMMessage,LLMResponse
from langchain_core.messages import BaseMessage


class BaseLLMClient:
    async def generate(
        self,
        messages: list[BaseMessage],
    ):
        raise NotImplementedError