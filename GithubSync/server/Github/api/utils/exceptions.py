"""Custom exception classes for GitHub API."""

from fastapi import HTTPException, status


class GitHubAPIError(HTTPException):
    """Base exception for GitHub API errors."""

    def __init__(
        self,
        status_code: int,
        detail: str,
        headers: dict = None,
    ):
        """Initialize exception.

        Args:
            status_code: HTTP status code
            detail: Error detail message
            headers: Optional response headers
        """
        super().__init__(
            status_code=status_code,
            detail=detail,
            headers=headers,
        )


class UnauthorizedException(GitHubAPIError):
    """Raised when authentication fails."""

    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
        )


class ForbiddenException(GitHubAPIError):
    """Raised when access is forbidden."""

    def __init__(self, detail: str = "Forbidden"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
        )


class NotFoundException(GitHubAPIError):
    """Raised when resource is not found."""

    def __init__(self, detail: str = "Not Found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )


class RateLimitException(GitHubAPIError):
    """Raised when rate limit is exceeded."""

    def __init__(self, detail: str = "Rate limit exceeded"):
        super().__init__(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=detail,
        )
