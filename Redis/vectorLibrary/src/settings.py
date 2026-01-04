import os


class Settings:
    def __init__(self):
        self.redis_host = os.getenv("REDIS_HOST", "localhost")
        self.redis_port = os.getenv("REDIS_PORT", "6379")
        self.redis_password = os.getenv("REDIS_PASSWORD", "")

    def get_redis_url(self):
        return f"redis://:{self.redis_password}@{self.redis_host}:{self.redis_port}"    