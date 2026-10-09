"""Runtime settings, read from the environment and an optional `.env` file."""


import os
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Final

from dotenv import load_dotenv

MODELS: Final[Mapping[str, str]] = {
    "jev": "typesafe/jev-1.13",
    "clef": "cloudflare/clef",
    "clef-flash": "cloudflare/clef-flash",
}
"""Short name used on the command line and in result files, mapped to the OpenRouter model id."""

DEFAULT_BASE_URL: Final = "https://openrouter.ai/api/alpha/decisions"


class ConfigError(RuntimeError):
    """Raised when required configuration is missing or invalid."""


@dataclass(frozen=True, slots=True)
class Settings:
    """Everything the CLI needs to talk to OpenRouter and find its files.

    Attributes:
        api_key: OpenRouter API key.
        base_url: Decisions API endpoint.
        timeout: Per-request timeout in seconds.
        max_retries: Retries on 429, 5xx and transport errors.
        concurrency: Requests in flight per model during a benchmark.
        data_dir: Where the dataset and sample are cached.
        results_dir: Where benchmark results and the report are written.
    """

    api_key: str
    base_url: str = DEFAULT_BASE_URL
    timeout: float = 30.0
    max_retries: int = 4
    concurrency: int = 8
    data_dir: Path = Path("data")
    results_dir: Path = Path("results")

    def __post_init__(self) -> None:
        if self.max_retries < 0:
            raise ConfigError(f"max_retries must be >= 0, got {self.max_retries}")
        if self.concurrency < 1:
            raise ConfigError(f"concurrency must be >= 1, got {self.concurrency}")

    @classmethod
    def from_env(cls, env_file: Path | None = Path(".env")) -> Settings:
        """Build settings from environment variables.

        Args:
            env_file: Optional dotenv file loaded first. Existing variables win.

        Returns:
            The resolved settings.

        Raises:
            ConfigError: If `OPENROUTER_API_KEY` is missing or a number is malformed.
        """
        if env_file is not None:
            load_dotenv(env_file)
        api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
        if not api_key:
            raise ConfigError(
                "OPENROUTER_API_KEY is not set. Copy .env.example to .env and add it."
            )
        try:
            return cls(
                api_key=api_key,
                base_url=os.environ.get("OPENROUTER_DECISIONS_URL", DEFAULT_BASE_URL),
                timeout=float(os.environ.get("DECISIONS_TIMEOUT", "30")),
                max_retries=int(os.environ.get("DECISIONS_MAX_RETRIES", "4")),
                concurrency=int(os.environ.get("DECISIONS_CONCURRENCY", "8")),
                data_dir=Path(os.environ.get("JEV_CLEF_DATA_DIR", "data")),
                results_dir=Path(os.environ.get("JEV_CLEF_RESULTS_DIR", "results")),
            )
        except ValueError as exc:
            raise ConfigError(f"Invalid numeric setting: {exc}") from exc
