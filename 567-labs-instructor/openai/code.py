import os
import instructor
from openai import OpenAI
from pydantic import BaseModel, Field

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = instructor.from_openai(OpenAI(api_key=OPENAI_API_KEY))

class File(BaseModel):
    file_name: str = Field(..., description = "The name of the file including the extension")
    body: str = Field(..., description = "Correct content of the file")

    def save(self):
        with open(self.file_name, "w") as f:
            f.write(self.body)


class Program(BaseModel):
    files: list[File] = Field(..., description = "List of files")

def develop(data: str) -> Program:
    return client.chat.completions.create(
        model = "gpt-4o-mini",
        temperature = 0.1,
        response_model=Program,
        messages=[
            {
                "role": "system",
                "content": "You are a world class programming AI capable of writing correct python scripts and modules. You will name files correct, include __init__.py files and write correct python code. with correct imports.",
            },
            {
                "role": "user",
                "content": data,
            },
        ],
        max_tokens=1000,
    )


if __name__ == "__main__":
    program = develop(
        """
        Create a fastapi app with a readme.md file and a main.py file with
        some basic math functions. the datamodels should use pydantic and
        the main.py should use fastapi. the readme.md should have a title
        and a description. The readme should contain some helpful infromation
        and a curl example"""
    )

    for file in program.files:
        print(file.file_name)
        print("-")
        print(file.body)
        print("\n\n\n")
    
    with open("program.json", "w") as f:
        f.write(program.model_dump_json())