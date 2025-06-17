import os
from openai import OpenAI
import time
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# Time the response
start_time = time.time()
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Tell me a three sentence bedtime story about a unicorn.",
)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")


print(response.id)
print(response)