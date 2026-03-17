# RAG Agent

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-green)](https://ollama.com/)
[![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-orange)](https://www.trychroma.com/)
[![Status](https://img.shields.io/badge/Project-Active-success)](#)

A lightweight Retrieval‑Augmented Generation (RAG) app that answers questions from **NCERT Class 12 Mathematics** using **local models only**. It runs entirely on your machine with **Ollama** for the LLM and **ChromaDB** as the vector store.

---

## ✨ Features

- **PDF ingestion**: Automatically reads and chunks all PDFs in the `pdfs/` directory.
- **Semantic search**: Uses `qwen3-embedding` to create embeddings and ChromaDB to retrieve the most relevant chunks.
- **Local LLM**: Generates answers with a local `qwen3.5-uncensored` model (configurable) through Ollama, keeping everything private and offline‑friendly.
- **Interactive CLI**: Clean command‑line chat experience tailored to NCERT maths.

---

## 📦 Prerequisites

- **Python 3.8+**
- **[Ollama](https://ollama.com/)** installed and running on your system.

### Required models

Either pull these models or update `config.py` to match your own setup:

```bash
ollama pull qwen3-embedding:0.6b
ollama pull jaahas/qwen3.5-uncensored:4b
```

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/rag-agent.git
cd rag-agent

# (Optional) create and activate a virtualenv
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧱 Usage

### 1. Build the index

1. Place your NCERT Class 12 Maths PDFs into the `pdfs/` directory.
2. Run the indexer:

   ```bash
   python rag.py
   ```

   This will:
   - Parse the PDFs
   - Chunk the text
   - Generate embeddings
   - Store everything in the `chroma_db/` directory using ChromaDB.

### 2. Start chatting

```bash
python main.py
```

Then, ask questions that are covered in the PDFs, and the agent will answer using the most relevant sections it retrieves.

Type `quit` to exit.

---

## ⚙️ Configuration

All configuration lives in `config.py`. You can tweak:

- **Models**: `EMBED_MODEL`, `LLM_MODEL`
- **Chunking**: `CHUNK_SIZE`, `CHUNK_OVERLAP`
- **Paths**: `CONTENT_DIR`, `DB_DIR`

---

## 🗂 Project structure

```text
.
├── main.py        # CLI chat entry point
├── rag.py         # PDF ingestion + index builder
├── generate.py    # Retrieval + answer generation logic
├── config.py      # Configuration settings
├── pdfs/          # Source NCERT PDFs
└── chroma_db/     # ChromaDB vector store (git-ignored)
```
