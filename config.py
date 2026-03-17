# config.py

# paths
CONTENT_DIR = "./pdfs"
DB_DIR = "./chroma_db"

# chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# models
EMBED_MODEL = "qwen3-embedding:0.6b"
LLM_MODEL = "qwen3.5:9b"

# vector database
COLLECTION_NAME = "ncert_math_12_vector"
