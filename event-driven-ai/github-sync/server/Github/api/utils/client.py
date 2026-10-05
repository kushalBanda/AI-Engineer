"""GitHub API client for making requests to GitHub REST API."""

from typing import Dict, Any, Optional
import httpx
from fastapi import HTTPException


class GitHubClient:
    """Client for interacting with GitHub REST API."""

    BASE_URL = "https://api.github.com"
    TIMEOUT = 30.0

    def __init__(self, token: str):
        """Initialize GitHub client with authentication token.

        Args:
            token: GitHub personal access token
        """
        self.token = token
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GithubSync-Client",
        }

    async def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make GET request to GitHub API.

        Args:
            endpoint: API endpoint path
            params: Query parameters

        Returns:
            Response JSON data

        Raises:
            HTTPException: If request fails
        """
        url = f"{self.BASE_URL}{endpoint}"
        async with httpx.AsyncClient(timeout=self.TIMEOUT) as client:
            response = await client.get(url, headers=self.headers, params=params)
            return self._handle_response(response)

    def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        """Handle GitHub API response.

        Args:
            response: httpx response object

        Returns:
            Response JSON data

        Raises:
            HTTPException: If response indicates an error
        """
        if response.status_code >= 400:
            try:
                error_data = response.json()
                message = error_data.get("message", "Unknown error")
            except Exception:
                message = response.text

            raise HTTPException(
                status_code=response.status_code,
                detail=message,
            )

        return response.json()
