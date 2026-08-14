from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(
    documents: list[dict],
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[dict]:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = []

    for document in documents:
        texts = splitter.split_text(document["text"])

        for text in texts:
            chunks.append({
                "text": text,
                "source": document["source"],
                "page": document["page"],
            })

    return chunks