from abc import ABC, abstractmethod

from AI_Developer_agent.backend.app.llm.models import LLMMessage,LLMResponse

class BaseLLMClient(ABC):
    @abstractmethod
    async def generate(self, messages:list[LLMMessage]):
        pass