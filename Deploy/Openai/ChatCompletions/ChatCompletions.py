from openai import OpenAI
from dotenv import load_dotenv
import time
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Time the response
start_time = time.time()
completion = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a three sentence bedtime story about a unicorn."}
    ]
)

print(completion.choices[0].message)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
