from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config

def get_embeddings_model():
    """get embeddings for the text"""
    return JinaEmbeddings(
        session=None,
        model_name=config.EMBEDDING_MODEL_NAME,
    )