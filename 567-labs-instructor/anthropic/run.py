import os
from pydantic import BaseModel
import anthropic
import instructor

from dotenv import load_dotenv
load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = instructor.from_anthropic(anthropic.Anthropic(api_key=ANTHROPIC_API_KEY))

class Properties(BaseModel):
    key: str
    value: str

class User(BaseModel):
    name: str
    age: int
    properties: list[Properties]

user = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1024,
    max_retries=0,
    messages=[
        {
            "role": "user",
            "content": "Create a user for a model with a name, age, and properties.",
        }
    ],
    response_model=User,
)

print(user.model_dump_json(indent=2))