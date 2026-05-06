
def add_metadata_to_chunks(chunks, source_file, page_info=None):
    """Add metadata to each chunk"""
    
    chunks_with_metadata = []
    
    for idx, chunk in enumerate(chunks):
        metadata = {
            "chunk_id": idx,
            "source": source_file,
            "chunk_text": chunk,
            "char_count": len(chunk),
            "page": page_info.get(idx) if page_info else None
        }
        chunks_with_metadata.append(metadata)
    
    return chunks_with_metadata

if __name__ == "__main__":
    sample_chunks = [
        "This is chunk 1",
        "This is chunk 2",
        "This is chunk 3"
    ]
    
    result = add_metadata_to_chunks(sample_chunks, "sample_paper.pdf")
    
    for meta in result:
        print(f"Chunk {meta['chunk_id']}: {meta['source']} - {meta['char_count']} chars")