from fastapi import FastAPI
from AI_Developer_agent.backend.app.api.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)