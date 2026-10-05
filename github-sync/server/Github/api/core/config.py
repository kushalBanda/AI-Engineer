"""Configuration module for GitHub API."""

import os
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # GitHub API Configuration
    github_token: str
    github_base_url: str = "https://api.github.com"
    github_api_timeout: float = 30.0

    # Database Configuration
    db_user: str = ""
    db_password: str = ""
    db_host: str = "localhost"
    db_port: int = 5432

    # AWS Configuration
    aws_access_id: str = ""
    aws_access_key: str = ""
    aws_region: str = "us-east-1"
    aws_s3_bucket: str = ""

    # Application Configuration
    app_title: str = "GitHub API"
    app_description: str = "FastAPI wrapper for GitHub REST API"
    app_version: str = "1.0.0"

    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = False

    # CORS Configuration
    cors_origins: list = ["*"]
    cors_credentials: bool = True
    cors_methods: list = ["*"]
    cors_headers: list = ["*"]

    class Config:
        """Pydantic config."""
        # Find .env in parent directory (GithubSync/) regardless of where the app is run from
        env_file = str(Path(__file__).parent.parent.parent.parent / ".env")
        case_sensitive = False


def get_settings() -> Settings:
    """Get application settings.

    Returns:
        Settings: Application configuration
    """
    return Settings()
