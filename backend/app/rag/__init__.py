
from AI_Developer_agent.backend.app.rag.rag import RAG
from AI_Developer_agent.backend.app.rag.retriever import Retriever
from AI_Developer_agent.backend.app.rag.vector_store import FAISSStore
from AI_Developer_agent.backend.app.rag.embeddings import EmbeddingModel

embedding_model = EmbeddingModel()
store = FAISSStore(384)
retriever = Retriever(store,embedding_model)