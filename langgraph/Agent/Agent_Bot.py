from typing import Any, Dict, List, Optional, Union, TypedDict
from langchain_core.messages import HumanMessage, BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()


class AgentState(TypedDict):
    messages: List[BaseMessage]

llm = ChatOpenAI(model = "gpt-4o-mini", temperature = 0)

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print(f"Agent: {response.content}")
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

agent.invoke({"messages": [HumanMessage(content="Hello, how are you?")]})