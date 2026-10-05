import os

import openai
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from config.settings import Settings

AGENT_MODEL = "gpt-4o-mini"
GRADER_MODEL = "gpt-4o-mini"
RAG_MODEL = "gpt-4o-mini"
REWRITE_MODEL = "gpt-4o-mini"
PAGEINDEX_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"


def get_openai_api_key() -> str:
    key = Settings().openai_api_key or os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it to your environment or .env file."
        )
    return key


def get_chat_model(model_name: str, temperature: float = 0, streaming: bool = True):
    return ChatOpenAI(
        api_key=get_openai_api_key(),
        model=model_name,
        temperature=temperature,
        streaming=streaming,
    )


def get_embeddings(model_name: str = EMBEDDING_MODEL):
    return OpenAIEmbeddings(api_key=get_openai_api_key(), model=model_name)


def get_async_openai_client():
    return openai.AsyncOpenAI(api_key=get_openai_api_key())
