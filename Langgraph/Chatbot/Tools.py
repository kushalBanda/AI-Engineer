from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper

api_wrapper = ArxivAPIWrapper(top_k_results = 2, doc_content_chars_max = 500)
arxiv_tool = ArxivQueryRun(api_wrapper = api_wrapper, description = "Query Arxiv Papers")


wikipedia = WikipediaAPIWrapper(top_k_results = 2, doc_content_chars_max = 500)
wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia, description = "Query Wikipedia Articles")

import os 
from dotenv import load_dotenv
load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


from langchain_community.tools.tavily_search import TavilySearchResults
tavily_tool = TavilySearchResults(api_key = TAVILY_API_KEY, max_results = 2)



tools = [arxiv_tool, wikipedia_tool, tavily_tool]
tools



from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model = "gpt-4o-mini", temperature = 0)
llm_with_tools = llm.bind_tools(tools = tools)

# llm_with_tools.invoke("What is the latest paper on quantum computing?")



## State Schema
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage, HumanMessage # Human message or AI message
from typing import Annotated # Labelling
from langgraph.graph.message import add_messages # Reducers in LangGraph


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]



# Entire Chatbot with LangGraph
from IPython.display import Image, display
from langgraph.graph.state import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition



# Nodes
def tool_calling_llm(state: State) -> State:
    """
    This function is used to call the LLM with the tools
    """
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

# Build the graph
builder = StateGraph(State)
builder.add_node('tool_calling_llm', tool_calling_llm)
builder.add_node('tools', ToolNode(tools))

# Edges
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges('tool_calling_llm', tools_condition)
builder.add_edge('tools', END)

# Compile the graph
graph = builder.compile()

result = graph.invoke({"messages": [HumanMessage(content="What is the latest paper on Machine Learning?")]})
result["messages"][-1].pretty_print()