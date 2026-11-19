# store chunk embedding in faiss

import os
from langchain_community.vectorstores import FAISS

from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model


# build vector store
def build_vector_store(chunks):
    """embed every chunk and build a searchable Faiss index in memory"""
    embeddings = get_embeddings_model()
    return FAISS.from_documents(chunks, embeddings)



# save vector store 

def save_vector_store(vector_store, path=config.VECTOR_STORE_PATH):
    """save the vector store to disk"""
    vector_store.save_local(path)


# load vector store
def load_vector_store(path=config.VECTOR_STORE_PATH):
    """load the vector store from disk"""
    embeddings_model = get_embeddings_model()
    return FAISS.load_local(path, embeddings_model, allow_dangerous_deserialization=True)


def vector_store_exists(path=config.VECTOR_STORE_PATH):
    """check if the vector store exists on disk"""
    return os.path.exists(os.path.join(path,"index.faiss"))


def get_retriever(vector_store,k:int=config.TOP_K_RESULTS):
    """get a retriever from the vector store"""
    return vector_store.as_retriever(search_kwargs={"k": k})