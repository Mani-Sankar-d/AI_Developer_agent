from typing import Any
from pydantic import BaseModel, Field

class LLMMessage(BaseModel):
    role: str
    content: str
    name: str | None = None
    tool_call: dict | None = None

class LLMResponse(BaseModel):
    content: str | None = None
    tool_calls: list[Any] = Field(default_factory=list)
    tool_results: list = Field(default_factory=list)

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str