
from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

def upload_to_pinecone(embeddings_data):
    """Upload embeddings to Pinecone"""
    
    vectors_to_upsert = []
    
    for item in embeddings_data:
        # Reduce embedding from 1536 to 512 dims (for our index)
        embedding = item["embedding"][:512]
        
        vector = {
            "id": f"chunk_{item['chunk_id']}",
            "values": embedding,
            "metadata": {
                "source": item["source"],
                "text": item["text"][:500]  # Store first 500 chars
            }
        }
        vectors_to_upsert.append(vector)
    
    # Upload in batches
    index.upsert(vectors=vectors_to_upsert)
    print(f"Uploaded {len(vectors_to_upsert)} vectors to Pinecone")

if __name__ == "__main__":
    # This will be tested after we integrate all steps
    print("Pinecone uploader ready")

    