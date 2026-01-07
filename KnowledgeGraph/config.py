import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.neo4j_uri = os.getenv("NEO4J_URI")
        self.neo4j_username = os.getenv("NEO4J_USERNAME")
        self.neo4j_password = os.getenv("NEO4J_PASSWORD")
        self.neo4j_database = os.getenv("NEO4J_DATABASE")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL")