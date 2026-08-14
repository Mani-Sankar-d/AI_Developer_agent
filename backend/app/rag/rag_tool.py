from langchain_core.tools import tool
from AI_Developer_agent.backend.app.rag.rag import RAG
from AI_Developer_agent.backend.app.rag import retriever,embedding_model

rag = RAG(
    retriever=retriever,
    embedding_model=embedding_model
)

@tool
def search_documents(query):
    """Search the uploaded documents for information relevant to the query."""
    return rag.get_context(query)