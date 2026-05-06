
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    reader = PdfReader(pdf_path)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text()
    
    return text

if __name__ == "__main__":
    # Test it
    text = extract_text_from_pdf("data/sample_paper.pdf")
    print(f"Extracted {len(text)} characters")
    print("\nFirst 500 chars:\n")
    print(text[:500])
    
