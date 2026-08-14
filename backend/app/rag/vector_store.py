from pathlib import Path
import json

import faiss
import numpy as np


class FAISSStore:
    def __init__(self, dimension: int, storage_dir: str = "rag_data"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

        self.index_path = self.storage_dir / "index.faiss"
        self.metadata_path = self.storage_dir / "metadata.json"

        if self.index_path.exists():
            self.index = faiss.read_index(str(self.index_path))
        else:
            self.index = faiss.IndexFlatIP(dimension)

        if self.metadata_path.exists():
            with open(self.metadata_path, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)
        else:
            self.metadata = {}

    def add(self, embeddings, chunks):
        embeddings = np.asarray(embeddings, dtype="float32")

        start_id = self.index.ntotal

        self.index.add(embeddings)

        for offset, chunk in enumerate(chunks):
            chunk_id = str(start_id + offset)

            self.metadata[chunk_id] = {
                "text": chunk["text"],
                "source": chunk["source"],
                "page": chunk["page"],
            }

        self._save()

    def search(self, query_embedding, k=5):
        query_embedding = np.asarray(
            [query_embedding],
            dtype="float32",
        )

        scores, indices = self.index.search(
            query_embedding,
            k,
        )

        results = []

        for score, index in zip(scores[0], indices[0]):
            if index == -1:
                continue

            metadata = self.metadata.get(str(index))

            if metadata is not None:
                results.append({
                    "score": float(score),
                    **metadata,
                })

        return results

    def _save(self):
        faiss.write_index(
            self.index,
            str(self.index_path),
        )

        with open(
            self.metadata_path,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                self.metadata,
                f,
                ensure_ascii=False,
                indent=2,
            )