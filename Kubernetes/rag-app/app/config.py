import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def _get_env(name: str, default: str = "") -> str:
    value = os.getenv(name)
    return value if value is not None else default


@dataclass(frozen=True)
class Settings:
    openai_api_key: str = _get_env("OPENAI_API_KEY")
    openai_embedding_model: str = "text-embedding-3-small"
    openai_llm_model: str = "gpt-4o-mini"
    rag_top_k: int = 5
    rag_max_context_chars: int = 4000
    rag_data_path: Path = Path("./data/index.json")


settings = Settings()
