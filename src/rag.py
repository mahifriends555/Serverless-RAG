# RAG core logic

from pinecone import Pinecone
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_rag(question, top_k=3):
    """Query RAG: retrieve + generate"""
    
    # Step 1: Embed the question
    print(f"Question: {question}")
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    )
    query_embedding = response.data[0].embedding[:512]
    
    # Step 2: Search Pinecone
    print(f"\nSearching Pinecone...")
    results = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
    
    # Extract retrieved texts
    retrieved_texts = [match["metadata"]["text"] for match in results["matches"]]
    print(f"Retrieved {len(retrieved_texts)} chunks")
    
    # Step 3: Generate answer using OpenAI
    print(f"\nGenerating answer...")
    context = "\n\n".join(retrieved_texts)
    
    prompt = f"""Context:
{context}

Question: {question}

Answer:"""
    
    answer_response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    answer = answer_response.choices[0].message.content
    return answer

if __name__ == "__main__":
    question = "What is attention mechanism?"
    answer = query_rag(question)
    print(f"\nAnswer:\n{answer}")
    