
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text, chunk_size=500, overlap=100):
    """Split text using LangChain's recursive splitter"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_text(text)

if __name__ == "__main__":
    sample = "Section A\n\nParagraph 1\n\nParagraph 2\n\nSection B\n\nParagraph 3"
    chunks = split_text(sample, chunk_size=100, overlap=20)
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i}: {len(chunk)} ")
        