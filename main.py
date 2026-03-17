from generate import answer_with_context, search


def main():
    print(f"{'-' * 25} RAG Agent {'-' * 25}\n")
    while True:
        query = input(f"YOU ('quit' to exit): ")
        if query.lower() == "quit":
            break

        print("\nSearching the vector database...")
        contexts = search(query=query, k=3)

        print(f"\nDEBUG: contexts={contexts}\n")
        print("Thinking...")
        answer = answer_with_context(query, contexts)

        print(f"\nBOT: {answer}\n")
        print(f"{'-' * 50}\n")


if __name__ == "__main__":
    main()
