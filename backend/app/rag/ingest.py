from AI_Developer_agent.backend.app.rag import retriever,embedding_model,store
from AI_Developer_agent.backend.app.rag.loader import load_pdf
from AI_Developer_agent.backend.app.rag.chunker import chunk_documents


def ingest_pdf(path: str):
    documents = load_pdf(path)
    chunks = chunk_documents(documents)

    texts = [chunk["text"] for chunk in chunks]

    embeddings = embedding_model.embed_documents(texts)

    store.add(embeddings, chunks)

# ingest_pdf("E:/Academics/PT.pdf")