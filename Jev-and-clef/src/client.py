"""Async client for OpenRouter's Decisions API.

Jev and Clef share one request shape, so this client knows nothing about
triage: it sends a state and questions, and returns the raw answers with
usage and latency.
"""


import asyncio
import time
from collections.abc import Mapping
from dataclasses import dataclass
from types import TracebackType
from typing import Any, Final, Self

import httpx

from config import Settings

JSONObject = dict[str, Any]

RETRY_STATUS: Final = frozenset({429, 500, 502, 503, 504})


class DecisionsError(RuntimeError):
    """Raised when the API returns an error or a response we cannot read."""


@dataclass(frozen=True, slots=True)
class Usage:
    """Token usage and cost reported by OpenRouter."""

    input_tokens: int = 0
    output_tokens: int = 0
    cost: float = 0.0

    @classmethod
    def from_json(cls, data: Mapping[str, Any]) -> Usage:
        """Read the `usage` object of a response, tolerating missing fields."""
        return cls(
            input_tokens=int(data.get("input_tokens", 0)),
            output_tokens=int(data.get("output_tokens", 0)),
            cost=float(data.get("cost", 0.0)),
        )


@dataclass(frozen=True, slots=True)
class DecisionResponse:
    """One successful Decisions call.

    Attributes:
        model: Model id the provider reports it used.
        answers: Answers keyed by question id, as returned by the API.
        usage: Tokens and cost.
        latency_ms: Wall time of the successful attempt.
    """

    model: str
    answers: JSONObject
    usage: Usage
    latency_ms: float


class DecisionsClient:
    """Thin async wrapper over `POST /api/alpha/decisions` with retries.

    Use it as an async context manager so the connection pool is closed:

        async with DecisionsClient(settings) as client:
            response = await client.decide("cloudflare/clef", state, questions)
    """

    def __init__(
        self, settings: Settings, transport: httpx.AsyncBaseTransport | None = None
    ) -> None:
        self._settings = settings
        self._http = httpx.AsyncClient(
            timeout=settings.timeout,
            transport=transport,
            headers={
                "Authorization": f"Bearer {settings.api_key}",
                "Content-Type": "application/json",
            },
        )

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self._http.aclose()

    async def decide(
        self, model: str, state: Mapping[str, Any], questions: Mapping[str, Any]
    ) -> DecisionResponse:
        """Ask a decision model a set of questions about one state.

        Args:
            model: OpenRouter model id, such as `typesafe/jev-1.13`.
            state: Context the model reasons over.
            questions: Question schema keyed by question id.

        Returns:
            The parsed response.

        Raises:
            DecisionsError: On a non-retryable error, exhausted retries, or a malformed body.
        """
        payload = {"model": model, "state": state, "questions": questions}
        attempts = self._settings.max_retries + 1
        for attempt in range(attempts):
            last_try = attempt == attempts - 1
            start = time.perf_counter()
            try:
                response = await self._http.post(self._settings.base_url, json=payload)
            except httpx.TransportError as exc:
                if last_try:
                    raise DecisionsError(f"{model}: {type(exc).__name__}: {exc}") from exc
            else:
                latency_ms = (time.perf_counter() - start) * 1000
                if response.status_code not in RETRY_STATUS or last_try:
                    return _parse(model, response, latency_ms)
            await asyncio.sleep(2**attempt)
        raise AssertionError("unreachable: the loop always returns or raises")


def _parse(model: str, response: httpx.Response, latency_ms: float) -> DecisionResponse:
    if response.is_error:
        raise DecisionsError(f"{model} returned HTTP {response.status_code}: {response.text[:500]}")
    try:
        data = response.json()
    except ValueError as exc:
        raise DecisionsError(f"{model} returned a non-JSON body") from exc
    answers = data.get("answers") if isinstance(data, dict) else None
    if not isinstance(answers, dict):
        raise DecisionsError(f"{model} response has no 'answers' object: {str(data)[:500]}")
    usage = data.get("usage")
    return DecisionResponse(
        model=str(data.get("model", model)),
        answers=answers,
        usage=Usage.from_json(usage if isinstance(usage, dict) else {}),
        latency_ms=latency_ms,
    )
