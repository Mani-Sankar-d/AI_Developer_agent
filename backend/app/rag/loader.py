from pathlib import Path
from pypdf import PdfReader


def load_pdf(path: str) -> list[dict]:
    reader = PdfReader(Path(path))

    documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text and text.strip():
            documents.append({
                "text": text,
                "source": str(path),
                "page": page_number,
            })

    return documents