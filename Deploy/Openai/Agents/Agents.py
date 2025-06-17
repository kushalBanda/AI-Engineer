from agents import Agent, Runner
import os
import time

from dotenv import load_dotenv
load_dotenv()   

api_key = os.getenv("OPENAI_API_KEY")

agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gpt-4.1-mini")

start_time = time.time()
result = Runner.run_sync(agent, "Tell me a three sentence bedtime story about a unicorn.")
print(result.final_output)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")