from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import os
from dotenv import load_dotenv

load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

client.recreate_collection(
    collection_name="sec10q_chunks",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

print("Collection created!")