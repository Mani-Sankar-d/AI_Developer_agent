from pydantic import BaseModel, Field
from AI_Developer_agent.backend.app.llm.models import LLMMessage
from typing import Any

class AgentState(BaseModel):
    user_message: str|None = None
    messages: list[LLMMessage] = Field(default_factory=list)
    final_response: str | None = None
    tool_calls: list[Any] = Field(default_factory=list)
    tool_results: list = Field(default_factory=list)
