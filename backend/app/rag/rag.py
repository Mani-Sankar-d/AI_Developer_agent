from AI_Developer_agent.backend.app.rag.embeddings import EmbeddingModel
from AI_Developer_agent.backend.app.rag.retriever import Retriever

class RAG:
    def __init__(self,retriever, embedding_model):
        self.retriever = retriever
        self.embedding_model = embedding_model

    def get_context(self, query, k=5):
        results = self.retriever.retrieve(query, k)
        return "\n\n".join(
            f"[Source: {result['source']}, Page: {result['page']}]\n"
            f"{result['text']}" for result in results
        )