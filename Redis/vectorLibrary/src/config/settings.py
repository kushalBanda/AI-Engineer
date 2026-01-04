import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.redis_host = os.getenv("REDIS_HOST")
        self.redis_port = os.getenv("REDIS_PORT")
        self.redis_password = os.getenv("REDIS_PASSWORD")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.pageindex_api_key = os.getenv("PAGEINDEX_API_KEY")
        
    def get_redis_url(self):
        return f"redis://:{self.redis_password}@{self.redis_host}:{self.redis_port}"