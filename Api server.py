from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from concurrent.futures import ThreadPoolExecutor
import textract
import uuid

# Initialize FastAPI app and components
app = FastAPI()
client = PersistentClient(db_path="chromadb")  # Define a path for ChromaDB storage
embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Executor for handling concurrent tasks
executor = ThreadPoolExecutor(max_workers=5)


def extract_text(file: UploadFile):
    # Extracts text from various file formats
    try:
        if file.filename.endswith('.pdf'):
            text = textract.process(file.file, method='pdftotext')
        elif file.filename.endswith('.docx'):
            text = textract.process(file.file, extension='docx')
        elif file.filename.endswith('.doc'):
            text = textract.process(file.file, extension='doc')
        elif file.filename.endswith('.txt'):
            text = file.file.read().decode('utf-8')
        else:
            return None
        return text.decode('utf-8') if isinstance(text, bytes) else text
    except Exception as e:
        print(f"Error extracting text from file: {e}")
        return None


@app.post("/ingest/")
async def ingest_document(file: UploadFile = File(...)):
    # Ingests document text into ChromaDB with embeddings
    text = extract_text(file)
    if not text:
        return JSONResponse(status_code=400, content={"message": "Unsupported file format"})

    # Create embeddings and store in ChromaDB
    embedding = embedding_model.encode(text, convert_to_tensor=True).tolist()
    doc_id = str(uuid.uuid4())
    client.insert_document(collection="documents", document_id=doc_id, text=text, embedding=embedding)

    return {"document_id": doc_id, "message": "Document ingested successfully"}


@app.get("/query/")
async def query_documents(query: str):
    # Query ChromaDB for relevant documents
    query_embedding = embedding_model.encode(query, convert_to_tensor=True).tolist()

    # Execute the query to find similar documents
    results = client.query(collection="documents", query_vector=query_embedding, top_k=5)
    documents = [{"document_id": result.document_id, "text": result.text, "similarity": result.similarity} for result in
                 results]

    return {"documents": documents}


# Run the FastAPI app with Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
