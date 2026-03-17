import os

import chromadb
import pymupdf as pdf
from ollama import Client

from config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    COLLECTION_NAME,
    CONTENT_DIR,
    DB_DIR,
    EMBED_MODEL,
)

chroma_client = chromadb.PersistentClient(path=DB_DIR)

client = Client()

pdfDocs = [f for f in os.listdir(CONTENT_DIR) if f.endswith(".pdf")]
pdfDocs.sort()

# ----------------------------------------------
# Parse PDFs
# ----------------------------------------------


def parse_pdf(file):
    doc = pdf.open(file)
    pages_text = []

    for page in doc:
        text = page.get_text("text")
        pages_text.append(text)

    doc.close()
    return "\n".join(pages_text)


def parse_all_pdfs(pdf_dir):
    texts = []

    for file in pdfDocs:
        full_path = os.path.join(pdf_dir, file)
        chapter_text = parse_pdf(full_path)
        texts.append(chapter_text)

    print(f"[PARSER] Parsed `{len(pdfDocs)}` PDF files in `{CONTENT_DIR}`")

    return "\n\n".join(texts)


# ----------------------------------------------
# Chunk Text
# ----------------------------------------------


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP):
    chunks = []
    start = 0
    text_len = len(text)

    while start < text_len:
        end = start + size
        chunk = text[start:end]
        chunks.append(chunk)

        start += size - overlap

    print(f"[CHUNKING] Processed `{len(chunks)}` chunks")

    return chunks


# ----------------------------------------------
# Embedding
# ----------------------------------------------


def embed_text(chunks: list[str]) -> list[list[float]]:
    embeddings = []
    total_chunks = len(chunks)

    for i, chunk in enumerate(chunks):
        response = client.embeddings(model=EMBED_MODEL, prompt=chunk)
        vector = response["embedding"]
        embeddings.append(vector)
        if (i + 1) % 100 == 0 or (i + 1) == total_chunks:
            print(f"  [EMBEDDING] Processed {i + 1}/{total_chunks} chunks")
    return embeddings


# ----------------------------------------------
# Store Embeddings in Vector Database
# ----------------------------------------------

collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)


def build_and_store_index():
    print("! Step 1/4: Parsing PDFs...")
    full_text = parse_all_pdfs(CONTENT_DIR)

    print(f"\n! Step 2/4: Chunking text (Total length: {len(full_text)} characters)...")
    chunks = chunk_text(full_text, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)

    print(f"\n! Step 3/4: Generating embeddings for {len(chunks)} chunks...")
    embeddings = embed_text(chunks)

    print("\n! Step 4/4: Storing data in Vector Database...")
    ids = [f"chunk-{i}" for i in range(len(chunks))]
    collection.add(ids=ids, documents=chunks, embeddings=embeddings)

    print("\n\n✅ Indexing complete!")


# ----------------------------------------------
# MAIN
# ----------------------------------------------

if __name__ == "__main__":
    build_and_store_index()
