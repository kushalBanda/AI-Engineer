
import json
from typing import Any

import httpx
import pytest

from client import DecisionsClient, DecisionsError, Usage
from config import Settings
from conftest import answers


def transport(
    *responses: httpx.Response | Exception,
) -> tuple[httpx.MockTransport, list[dict[str, Any]]]:
    queue = list(responses)
    sent: list[dict[str, Any]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append({"headers": dict(request.headers), "body": json.loads(request.content)})
        item = queue.pop(0)
        if isinstance(item, Exception):
            raise item
        return item

    return httpx.MockTransport(handler), sent


OK = httpx.Response(
    200,
    json={
        "model": "cloudflare/clef",
        "answers": answers(),
        "usage": {"input_tokens": 421, "output_tokens": 70, "cost": 1.7e-5},
    },
)


async def test_decide_sends_payload_and_parses(settings: Settings) -> None:
    mock, sent = transport(OK)
    async with DecisionsClient(settings, mock) as client:
        response = await client.decide("cloudflare/clef", {"ticket": "hi"}, {"q": {"type": "noul"}})

    assert sent[0]["body"] == {
        "model": "cloudflare/clef",
        "state": {"ticket": "hi"},
        "questions": {"q": {"type": "noul"}},
    }
    assert sent[0]["headers"]["authorization"] == "Bearer test-key"
    assert response.model == "cloudflare/clef"
    assert response.answers["category"]["choice"] == "REFUND"
    assert response.usage == Usage(421, 70, 1.7e-5)
    assert response.latency_ms >= 0


async def test_retries_on_429_and_transport_errors(settings: Settings) -> None:
    mock, sent = transport(httpx.Response(429), httpx.ConnectError("down"), OK)
    async with DecisionsClient(settings, mock) as client:
        response = await client.decide("m", {}, {})
    assert len(sent) == 3
    assert response.answers


async def test_gives_up_after_max_retries(settings: Settings) -> None:
    mock, sent = transport(*(httpx.Response(503, text="busy") for _ in range(3)))
    async with DecisionsClient(settings, mock) as client:
        with pytest.raises(DecisionsError, match="HTTP 503"):
            await client.decide("m", {}, {})
    assert len(sent) == settings.max_retries + 1


async def test_transport_error_on_last_try_raises(settings: Settings) -> None:
    mock, _ = transport(*(httpx.ConnectError("down") for _ in range(3)))
    async with DecisionsClient(settings, mock) as client:
        with pytest.raises(DecisionsError, match="ConnectError"):
            await client.decide("m", {}, {})


async def test_client_error_is_not_retried(settings: Settings) -> None:
    mock, sent = transport(httpx.Response(400, text="bad question"))
    async with DecisionsClient(settings, mock) as client:
        with pytest.raises(DecisionsError, match="HTTP 400"):
            await client.decide("m", {}, {})
    assert len(sent) == 1


@pytest.mark.parametrize(
    ("response", "message"),
    [
        (httpx.Response(200, text="not json"), "non-JSON"),
        (httpx.Response(200, json={"model": "m"}), "no 'answers'"),
        (httpx.Response(200, json=[1, 2]), "no 'answers'"),
    ],
)
async def test_malformed_body(settings: Settings, response: httpx.Response, message: str) -> None:
    mock, _ = transport(response)
    async with DecisionsClient(settings, mock) as client:
        with pytest.raises(DecisionsError, match=message):
            await client.decide("m", {}, {})


async def test_missing_usage_defaults_to_zero(settings: Settings) -> None:
    mock, _ = transport(httpx.Response(200, json={"answers": {}}))
    async with DecisionsClient(settings, mock) as client:
        response = await client.decide("fallback-model", {}, {})
    assert response.usage == Usage()
    assert response.model == "fallback-model"
