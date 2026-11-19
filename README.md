# HR Policy Assistant

A Retrieval-Augmented Generation (RAG) application that answers questions about HR policies using document retrieval and an LLM-powered agent.

## Tech Stack

- Python
- LangChain
- Groq — `openai/gpt-oss-20b`
- Jina Embeddings — `jina-embeddings-v2-base-en`
- FAISS — vector storage and similarity search
- Streamlit — chat interface

## Features

- HR policy document loading and processing.
- Text chunking with configurable size and overlap.
- Semantic embeddings using Jina.
- Local FAISS vector database.
- Retrieval of the top 3 relevant chunks.
- LangChain agent with an HR policy search tool.
- Streamlit chat interface and CLI application.
- Local persistence and reuse of the vector index.

## Project Structure

```text
.
├── app.py
├── main.py
├── requirements.txt
├── data/
│   └── hr_policy.txt
└── hr_assistant/
    ├── agent.py
    ├── config.py
    ├── document_loader.py
    ├── embeddings.py
    ├── llm.py
    ├── pipeline.py
    ├── splitter.py
    ├── tools.py
    └── vector_store.py
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/TatTva-asi/rag-basic-project-.git
cd rag-basic-project-
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
Jina_API_KEY=your_jina_api_key
```

Never commit API keys or `.env` files.

### 5. Add your HR document

Place your HR policy document at:

```text
data/hr_policy.txt
```

## Run the Project

Start the Streamlit application:

```bash
streamlit run app.py
```

Run the CLI application:

```bash
python main.py
```

On the first run, the application processes the document, generates embeddings, and builds a FAISS index locally. Subsequent runs reuse the saved index.

## RAG Workflow

1. Load the HR policy document.
2. Split the document into smaller chunks.
3. Generate embeddings using Jina.
4. Store embeddings in FAISS.
5. Retrieve relevant chunks for a user query.
6. Pass the retrieval tool to the LangChain agent.
7. Generate a context-aware response using Groq.

## Configuration

| Parameter | Value |
|---|---|
| LLM | `openai/gpt-oss-20b` |
| Embedding model | `jina-embeddings-v2-base-en` |
| Temperature | `0.3` |
| Maximum output tokens | `1024` |
| Chunk size | `500` |
| Chunk overlap | `50` |
| Top-K retrieval | `3` |

## Security Notes

- The FAISS index is generated locally and excluded from Git.
- HR policy documents should not be committed if they contain confidential information.
- FAISS loading currently enables dangerous deserialization. Only load trusted index files.
- This is a learning project and requires additional security, evaluation, and access-control work before real enterprise deployment.

## Future Improvements

- Source citations and metadata filtering.
- PDF and DOCX document ingestion.
- Retrieval evaluation.
- Better error handling and observability.
- Authentication and access control.

## License

No license has been specified yet.
