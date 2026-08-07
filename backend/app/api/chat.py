from fastapi import APIRouter
from AI_Developer_agent.backend.app.agent.executor import AgentExecutor
from AI_Developer_agent.backend.app.agent.models import ChatRequest, ChatResponse
from AI_Developer_agent.backend.app.core.config import settings
from AI_Developer_agent.backend.app.llm.gemini_client import GeminiClient
from AI_Developer_agent.backend.app.globals import agentstate
from AI_Developer_agent.backend.app.llm.models import LLMMessage

router = APIRouter()
llm = GeminiClient(
    api_key = settings.GEMINI_API_KEY,
    model = settings.GEMINI_MODEL
)
executor = AgentExecutor(llm)

@router.post("/chat",response_model=ChatResponse)
async def chat(req: ChatRequest):
    agentstate.messages.append(LLMMessage(role="user",content=req.message))
    response = await executor.run(agentstate)
    return {"response":response}