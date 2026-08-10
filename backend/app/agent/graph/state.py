from typing import TypedDict

from AI_Developer_agent.backend.app.llm.models import LLMMessage


class AgentState(TypedDict):
    messages:list[LLMMessage]