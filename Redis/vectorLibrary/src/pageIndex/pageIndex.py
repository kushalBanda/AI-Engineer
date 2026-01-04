import openai
from pageindex import PageIndexClient
import pageindex.utils as utils

from config.settings import Settings

PAGEINDEX_API_KEY = Settings().pageindex_api_key
pi_client = PageIndexClient(api_key = PAGEINDEX_API_KEY)


async def call_llm(prompt, model="gpt-4o-mini", temperature=0):
    client = openai.AsyncOpenAI(api_key=Settings().openai_api_key)
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

