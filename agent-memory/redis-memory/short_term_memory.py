"""Short-term memory agent using LangGraph + Redis.

Prereqs (example):
!pip install langchain_openai langgraph langgraph-checkpoint-redis redis

Ensure Redis is running at REDIS_URI before running this script.
"""

from __future__ import annotations

import getpass
import os
from typing import Literal

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.redis import RedisSaver
from langgraph.prebuilt import create_react_agent


REDIS_URI = os.environ.get("REDIS_URI", "redis://localhost:6379")
CHAT_MODEL = os.environ.get("CHAT_MODEL", "gpt-4o-mini")


def _set_env(var: str) -> None:
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in nyc"
    if city == "sf":
        return "It's always sunny in sf"
    raise AssertionError("Unknown city")


def build_agent():
    tools = [get_weather]
    model = ChatOpenAI(model=CHAT_MODEL, temperature=0)
    with RedisSaver.from_conn_string(REDIS_URI) as checkpointer:
        checkpointer.setup()
        return create_react_agent(model, tools=tools, checkpointer=checkpointer)


def demo(graph) -> None:
    config = {"configurable": {"thread_id": "user2322"}}
    res = graph.invoke({"messages": [("human", "Which state did I ask?")]}, config)
    print(res["messages"][-1].content)


if __name__ == "__main__":
    _set_env("OPENAI_API_KEY")
    graph = build_agent()
    demo(graph)
