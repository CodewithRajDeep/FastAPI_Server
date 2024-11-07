## Title: FastAPI RAG Server

## <a name="description">Description</a>
A lightweight FastAPI server implementing Retrieval-Augmented Generation (RAG) capabilities, utilizing ChromaDB for document storage and querying,
with sentence-transformers for embedding generation. The server supports document ingestion and query functionalities with non-blocking API endpoints
and efficient concurrency handling.

  <div>
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="github" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="python" />
  </div>


Watch the video 👇

<a href="https://drive.google.com/file/d/1HA7-jhe63TA3GfF30_cFwk-2S4BZQOIh/view">
    <img src="https://drive.google.com/uc?export=view&id=157XnzredVHGA71wu9-cSrrs5rYgjCpOf" width="320" height="240" />
</a>

## 📋 <a name="table">Table of Contents</a>

1. 🤖 [Introduction](#description)
2. ⚙️ [Tech Stack](#tech-stack)
3. 🔋 [Features](#features)
4. 🤸 [Quick Start](#quick-start)
5. 🕸️ [Setup .env variables](#snippet)
6. 🦉[Work Demonstration](#work-demonstration)

##  <a name="work-demonstration"> 🦉Work Demonstration </a>
<img src="" width="320" height="240" />

## <a name="tech-stack">⚙️ Tech Stack</a>

- FastAPI
- ChromaDB
- Sentence-Transformers
- Uvicorn
- Pytest
- 
## <a name="features">🔋 Features</a>

👉 **Document Ingestion:** Upload PDF, DOC, DOCX, or TXT files and store document embeddings in ChromaDB.
👉 **Querying:** Retrieve documents based on semantic similarity to a query.
👉 **Concurrency:**  Non-blocking endpoints with concurrent document handling.

## <a name="quick-start">🤸 Getting Started </a>
1. Clone the repository
bash
Copy code
```git clone https://github.com/yourusername/fastapi-rag-server.git
cd fastapi-rag-server
```
2. Set up a virtual environment
bash
```
Copy code
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
4. Install dependencies
bash
```
Copy code
pip install -r requirements.txt
```
Requirements
The requirements.txt should contain:
```
plaintext
Copy code
fastapi
uvicorn
chromadb
sentence-transformers
pypdf
python-docx
textract
```
Running the Server
1. Start the FastAPI server
Use Uvicorn to run the FastAPI server.

bash
```
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
The server will be available at http://localhost:8000.
```
2. API Endpoints
Ingest Document
Endpoint: POST /ingest/
Description: Uploads a document (PDF, DOC, DOCX, TXT) and stores it in ChromaDB.
Parameters: file (UploadFile) - The document file to be ingested.
Example:
bash
Copy code
```
curl -X 'POST' \
  'http://localhost:8000/ingest/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@path_to_your_file.pdf'
```
Query Documents
Endpoint: GET /query/
Description: Queries documents based on semantic similarity to the provided text.
Parameters: query (str) - The query text.

bash
Copy code
```
curl -X 'GET' \
  'http://localhost:8000/query/?query=your_query_text' \
  -H 'accept: application/py'
```
4. Testing
Access the interactive API docs at http://localhost:8000/docs or the redoc documentation at http://localhost:8000/redoc.

Contributing
Fork the repository
Create a new branch for your feature or bug fix:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Add new feature"
Push to the branch:
bash
Copy code
git push origin feature-name
Create a pull request

## Contribution Guidelines: 
Guidelines for contributing to the project.

**Reporting Issues:**

Search for existing issues: Before creating a new issue, search the issue tracker to see if the problem has already been reported.
Provide clear and concise information: When creating a new issue, please include as much detail as possible, such as:
Clear description of the problem
Steps to reproduce the issue
Expected behavior
Actual behavior
Screenshots or logs (if applicable)
Use issue templates: If available, use the provided issue templates to structure your report.

**Submitting Pull Requests:**

Fork the repository: Create a fork of the project on your GitHub account.
Create a new branch: Create a new branch based on the main branch or a feature branch.
Make changes: Implement your changes and commit them with clear commit messages.
Push changes to your fork: Push your changes to your forked repository.
Open a Pull Request: Create a pull request from your branch to the main repository.
Provide details: Clearly describe the changes you've made and the benefits they bring.
Address code review feedback: Be open to feedback and make necessary changes.

**Testing:**

Write unit tests for any new features or bug fixes.
Ensure existing tests  pass after your changes.

## License
Issued : Copyright (c)| 2024 Deep Raj 

## Memes: 
<img src="https://i.gifer.com/origin/ea/ea04580a05ae61739fefe6b70f17a4c3.gif" width="256" height="256"/>
<img src="https://i0.wp.com/www.animefeminist.com/wp-content/uploads/2018/06/type-happy-dog-motivate.gif?fit=309%2C233&ssl=1" width="256" height="256"/>
<img src="https://i0.wp.com/www.animefeminist.com/wp-content/uploads/2018/06/pitch-baseball-explode-nichijou.gif?resize=500%2C281&ssl=1" width="256" height="256"/>


