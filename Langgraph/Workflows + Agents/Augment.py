import os 
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

class SearchQuery(BaseModel):
    search_query: str = Field(None, description = "Query that is optimized web search")
    justifications: str = Field(None, description = "Justifications for the search query")

# Augument the LLM with schema for structure output
structured_llm = llm.with_structured_output(SearchQuery)

# Invoke the augmented LLM
output = structured_llm.invoke("How does Calcium CT score relate to high cholesterol?")

print(output)

# Define a tool
def multiply(a: int, b: int) -> int:
    return a * b

# Augment the LLM with tools
llm_with_tools = llm.bind_tools([multiply])

# Invoke the augmented LLM
msg = llm_with_tools.invoke("What is 10 * 20?")

print(msg)
