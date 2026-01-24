from typing import List
from openai import OpenAI


class OpenAIEmbedder:
    def __init__(self, api_key: str, model: str) -> None:
        self._client = OpenAI(api_key=api_key)
        self._model = model

    def embed(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []
        response = self._client.embeddings.create(
            model=self._model,
            input=texts,
            encoding_format="float",
        )
        return [item.embedding for item in response.data]
