""" connect llm to brain of assitant"""

from langchain_groq import ChatGroq
from hr_assistant import config
def get_llm():
    """get the llm model"""
    return ChatGroq(model=config.LLM_MODEL_NAME,temperature=config.LLM_TEMPERATURE,max_tokens=config.LLM_MAX_OUTPUT_TOKENS)