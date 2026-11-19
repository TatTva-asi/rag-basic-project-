""" Read the raw document from the data folder"""

from langchain_community.document_loaders import TextLoader
from hr_assistant import config

def load_document(file_path=config.DATA_FILE_PATH):
    """load a .txt file and return it as list of langchain documents"""

    loader=TextLoader(file_path,encoding="utf-8")
    return loader.load()

