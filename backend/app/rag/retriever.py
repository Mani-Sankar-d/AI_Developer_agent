from AI_Developer_agent.backend.app.rag.loader import load_pdf
from AI_Developer_agent.backend.app.rag.chunker import chunk_documents


class Retriever:
    def __init__(self,store,embedding_model):
        self.store = store
        self.embedding_model = embedding_model
    def retrieve(self, query, k):
        query_embedding = self.embedding_model.embed_query(query)
        return self.store.search(query_embedding,k)