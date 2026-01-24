from typing import Iterable
from openai import OpenAI


class OpenAILLM:
    def __init__(self, api_key: str, model: str) -> None:
        self._client = OpenAI(api_key=api_key)
        self._model = model

    def generate(self, prompt: str) -> str:
        response = self._client.responses.create(
            model=self._model,
            input=prompt,
        )
        return _extract_text(response)


def _extract_text(response: object) -> str:
    if hasattr(response, "output_text"):
        text = getattr(response, "output_text")
        if isinstance(text, str) and text.strip():
            return text

    output = getattr(response, "output", None)
    if not output:
        return ""

    chunks: Iterable[object] = output if isinstance(output, list) else [output]
    parts = []
    for item in chunks:
        content = getattr(item, "content", None)
        if not content:
            continue
        for block in content:
            block_type = getattr(block, "type", "")
            if block_type in {"output_text", "text"}:
                text = getattr(block, "text", None)
                if isinstance(text, str):
                    parts.append(text)
    return "".join(parts).strip()
