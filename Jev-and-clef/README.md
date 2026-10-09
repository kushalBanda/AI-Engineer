# Jev and Clef

[← AI Engineer](../README.md)

**Level:** 🟡 Intermediate · **Type:** `Project` · Commands run from `Jev-and-clef/`.

Customer support triage with System One decision models, benchmarked on real labelled tickets.

[Jev](https://openrouter.ai/docs/guides/community/jev) (TypeSafe) and [Clef](https://openrouter.ai/cloudflare/clef) (Cloudflare) are decision models. They don't write text. You send a state and typed questions, and each answer comes back as a probability in one forward pass. Both share one request shape on OpenRouter's Decisions API, so swapping models is one string.

Each ticket gets four questions in a single request:

| Question | Type | Labelled? |
| :--- | :--- | :--- |
| `category` | `choice`, 11 options | Yes |
| `intent` | `choice`, 27 options | Yes |
| `urgency` | `score`, low to critical | No, models are compared for agreement |
| `needs_human` | `noul`, probability of yes | No, models are compared for agreement |

Tickets come from the [Bitext customer support dataset](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset) (26,872 rows, CDLA-Sharing-1.0). It is downloaded at run time, not committed.

Layout:

```text
src/
├── config.py      Settings from env, model registry
├── client.py      Async Decisions API client with retry on 429 and 5xx
├── questions.py   The four questions and their options
├── triage.py      Typed answers, one-ticket triage, routing rule
├── dataset.py     Bitext download, stratified sample across intents
├── bench.py       Resumable benchmark, results/<model>.jsonl
├── report.py      Accuracy, latency, cost, thresholds, calibration, agreement
└── cli.py         jev-clef sample | triage | bench | report
tests/             pytest suite, no network
```

Models: `typesafe/jev-1.13`, `cloudflare/clef` (27B), `cloudflare/clef-flash` (9B).

## Run

```bash
cd Jev-and-clef
uv sync
cp .env.example .env          # add OPENROUTER_API_KEY

uv run jev-clef triage "I was charged twice and want my money back today"

uv run jev-clef sample        # 100 tickets, --size to change
uv run jev-clef bench         # --limit 20 to try a small run first
uv run jev-clef report        # writes results/report.md
```

A 100-ticket run is 300 requests and costs about 1.5 cents. `bench` resumes where it stopped.

## Develop

```bash
uv run pytest
uv run mypy --strict src tests
uv run ruff check src tests && uv run black --check src tests
```

## Depends on

- An [OpenRouter](https://openrouter.ai) API key. No TypeSafe or Cloudflare account needed.

## Credits

The triage idea follows [Customer-Support-Triage-with-Jev](https://github.com/entbappy/Customer-Support-Triage-with-Jev).
