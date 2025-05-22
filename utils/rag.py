# from utils.model import embedder, client, tokenizer, llm_model, COLLECTION_NAME
from utils.model import embedder, client, gpt4all_model, COLLECTION_NAME

def retrieve_relevant_chunks(question, top_k=5):
    emb = embedder.encode(question).tolist()
    results = client.search(collection_name=COLLECTION_NAME, query_vector=emb, limit=top_k)

    for hit in results:
        print(hit.payload)

    return [
        {
            "text": hit.payload.get("text", ""),
            "doc_name": hit.payload.get("doc_name", ""),
            "chunk_id": hit.payload.get("chunk_id", "")
        }
        for hit in results
    ]

def generate_answer(question, chunks):
    chunk_texts = [chunk.get("text", "") for chunk in chunks]
    context = "\n\n".join(chunk_texts)
    prompt = f"Context:\n{context}\n\nQuestion:\n{question}\nAnswer:"
    response = gpt4all_model.generate(prompt)
    return response