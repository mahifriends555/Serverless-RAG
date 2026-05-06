
from pdf_extractor import extract_text_from_pdf
from chunker import split_text
from metadata_handler import add_metadata_to_chunks
from embeddings import embed_chunks
from pinecone_uploader import upload_to_pinecone

def run_pipeline(pdf_path):
    """Run complete RAG pipeline"""
    
    print("1. Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)
    print(f"   Extracted {len(text)} characters")
    
    print("\n2. Chunking text...")
    chunks = split_text(text, chunk_size=500, overlap=100)
    print(f"   Created {len(chunks)} chunks")
    
    print("\n3. Adding metadata...")
    chunks_meta = add_metadata_to_chunks(chunks, pdf_path)
    print(f"   Added metadata to {len(chunks_meta)} chunks")
    
    print("\n4. Embedding chunks...")
    embeddings_data = embed_chunks(chunks_meta)
    print(f"   Embedded {len(embeddings_data)} chunks")
    
    print("\n5. Uploading to Pinecone...")
    upload_to_pinecone(embeddings_data)
    
    print("\n✓ Pipeline complete!")

if __name__ == "__main__":
    run_pipeline("data/sample_paper.pdf")
    