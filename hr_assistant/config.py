""" all settings for the app live here , in one place"""

import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
Jina_API_KEY=os.getenv("Jina_API_KEY")


DATA_FILE_PATH=os.path.join("data","hr_policy.txt")

VECTOR_STORE_PATH=os.path.join("data","faiss_index")

LLM_MODEL_NAME="openai/gpt-oss-20b"
EMBEDDING_MODEL_NAME="jina-embeddings-v2-base-en"

LLM_TEMPERATURE=0.3
LLM_MAX_OUTPUT_TOKENS=1024

CHUNK_SIZE=500
CHUNK_OVERLAP=50

TOP_K_RESULTS=3

SYSTEM_PROMPT=(
     """you are friendly hr assistant always use search_hr_policy to look up facts if ans is not in search results say idk instead of guessing"""
)

def check_api_keys():
    """stop early if a required api key is missing"""
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set in environment variables.")
    if not Jina_API_KEY:
        raise ValueError("Jina_API_KEY is not set in environment variables.")