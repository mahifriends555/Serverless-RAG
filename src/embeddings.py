
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_chunks(chunks_with_metadata):
    """Embed each chunk using OpenAI"""
    
    embeddings_data = []
    
    for meta in chunks_with_metadata:
        # Embed the chunk text
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=meta["chunk_text"]
        )
        
        embedding = response.data[0].embedding
        
        # Store with metadata
        embeddings_data.append({
            "chunk_id": meta["chunk_id"],
            "source": meta["source"],
            "text": meta["chunk_text"],
            "embedding": embedding,
            "metadata": meta
        })
    
    return embeddings_data

if __name__ == "__main__":
    sample = [
        {"chunk_id": 0, "source": "test.pdf", "chunk_text": "Hello world"},
        {"chunk_id": 1, "source": "test.pdf", "chunk_text": "This is a test"}
    ]
    
    result = embed_chunks(sample)
    print(f"Embedded {len(result)} chunks")
    print(f"Embedding size: {len(result[0]['embedding'])}")