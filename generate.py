import chromadb
from ollama import Client

from config import COLLECTION_NAME, DB_DIR, EMBED_MODEL, LLM_MODEL

print(
    f"DEBUG: COLLECTION_NAME={COLLECTION_NAME}, DB_DIR={DB_DIR}, EMBED_MODEL={EMBED_MODEL}, LLM_MODEL={LLM_MODEL}\n"
)

chroma_client = chromadb.PersistentClient(path=DB_DIR)
collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)

embed_client = Client()
gen_client = Client()


def embed_query(query: str) -> list[float]:
    response = embed_client.embeddings(model=EMBED_MODEL, prompt=query)
    return response["embedding"]


def search(query: str, k: int = 3):
    q_vector = embed_query(query)
    results = collection.query(query_embeddings=[q_vector], n_results=k)
    return results["documents"][0]


def answer_with_context(question: str, contexts: list[str]) -> str:
    ctx = "\n\n".join(contexts)

    prompt = (
        "You are a helpful Class 12 mathematics tutor. "
        "Use ONLY the NCERT-based context below to answer.\n\n"
        f"Context:\n{ctx}\n\n"
        f"Question: {question}\n\n"
        "Answer clearly and concisely:"
    )

    response = gen_client.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]


if __name__ == "__main__":
    query = input("SEARCH QUERY: ")
    query = "What are functions and relations" if query == "" else query
    print(f"SEARCHING QUERY `{query}`...")
    print(f"\nRESULTS: {search(query=query, k=3)}")
