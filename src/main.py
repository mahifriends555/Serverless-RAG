# Cloud Function entry

import functions_framework
from rag import query_rag
import json

@functions_framework.http
def rag_endpoint(request):
    """HTTP endpoint for RAG queries"""
    
    try:
        # Get question from request
        request_json = request.get_json()
        question = request_json.get("question")
        
        if not question:
            return {"error": "No question provided"}, 400
        
        # Run RAG
        answer = query_rag(question, top_k=3)
        
        return {
            "question": question,
            "answer": answer
        }, 200
    
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    # Test locally
    test_request = type('obj', (object,), {
        'get_json': lambda: {"question": "What is transformer?"}
    })()
    
    result, status = rag_endpoint(test_request)
    print(f"Status: {status}")
    print(f"Result: {json.dumps(result, indent=2)}")
    