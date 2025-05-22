import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from gpt4all import GPT4All

# Load environment variables from .env file
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME")

# Embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Qdrant Client
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

# GPT4All local model
gpt4all_model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", device='cpu')