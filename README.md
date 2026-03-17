# RAG Agent

A Retrieval-Augmented Generation (RAG) application that answers questions based on NCERT Class 12 Mathematics textbooks. It uses local LLMs via Ollama for privacy and offline capability, with ChromaDB for vector storage.

## Features

- **PDF Ingestion**: Automatically parses and chunks PDF documents from the `pdfs/` directory.
- **Vector Search**: Uses `qwen3-embedding` to generate embeddings and ChromaDB for semantic search.
- **Local LLM**: Generates answers using `qwen3.5-uncensored` (configurable) running locally via Ollama.
- **Interactive CLI**: Simple command-line interface for chatting with your documents.

## Prerequisites

- **Python 3.8+**
- **[Ollama](https://ollama.com/)**: Must be installed and running.

### Required Models

You need to pull the specific models used in the configuration (or update `config.py` to match your available models):

```bash
ollama pull qwen3-embedding:0.6b
ollama pull jaahas/qwen3.5-uncensored:4b
```

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/rag-agent.git
    cd rag-agent
    ```

2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Build the Index

First, you need to process the PDFs and store their embeddings in the vector database.

1.  **Add PDFs**: Place your PDF documents into the `pdfs/` directory.
2.  **Run the Indexer**:

```bash
python rag.py
```
*This will parse the PDFs, chunk the text, generate embeddings, and save them to the `chroma_db/` directory.*

### 2. Start the Chat

Once the index is built, you can start the interactive chat agent:

```bash
python main.py
```

### 3. Ask Questions

The agent will prompt you for input. Ask questions related to the content in the PDFs:

```text
YOU: What is a relation?
Thinking...
BOT: A relation R in a set A is a subset of the cartesian product A x A. It represents a relationship between elements of the set.
```

Type `quit` to exit the application.

## Configuration

You can modify `config.py` to change:
-   **Models**: `EMBED_MODEL` and `LLM_MODEL`.
-   **Chunking**: `CHUNK_SIZE` and `CHUNK_OVERLAP`.
-   **Paths**: `CONTENT_DIR` and `DB_DIR`.

## Project Structure

-   `main.py`: Entry point for the chat interface.
-   `rag.py`: Script to ingest PDFs and build the vector database.
-   `generate.py`: Logic for searching and generating answers.
-   `config.py`: Configuration settings.
-   `pdfs/`: Directory containing source PDF documents.
-   `chroma_db/`: Directory where the vector database is stored (ignored in git).
