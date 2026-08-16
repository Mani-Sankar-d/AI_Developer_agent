from langchain_google_genai import ChatGoogleGenerativeAI
from AI_Developer_agent.backend.app.core.settings import settings
llm = ChatGoogleGenerativeAI(
        model=settings.MODEL,
        api_key=settings.KEY,
    )