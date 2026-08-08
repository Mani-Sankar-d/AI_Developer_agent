from typing import Any
from pydantic import BaseModel, Field

class LLMMessage(BaseModel):
    role: str
    content: str | None = None
    name: str | None = None
    tool_call: dict | None = None
    raw_content: Any = None

class LLMResponse(BaseModel):
    content: str | None = None
    tool_calls: list[Any] = Field(default_factory=list)
    raw_content: Any = None

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str