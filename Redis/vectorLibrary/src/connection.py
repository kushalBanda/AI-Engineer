import os
from redis import Redis
from settings import Settings

class Connection:
    def __init__(self):
        self.settings = Settings()
        self.redis_client = Redis(url=self.settings.get_redis_url())

    def ping(self):
        return self.redis_client.ping()
