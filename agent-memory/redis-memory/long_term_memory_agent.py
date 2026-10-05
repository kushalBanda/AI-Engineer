"""Long-term memory agent using LangGraph + Redis.

Prereqs (example):
!pip install langchain_openai langgraph langgraph-checkpoint-redis redis

Ensure Redis is running at REDIS_URI before running this script.
"""

from __future__ import annotations

import getpass
import os
import uuid
from typing import Iterable

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.runnables import RunnableConfig
from langgraph.graph import MessagesState, StateGraph, START
from langgraph.checkpoint.redis import RedisSaver
from langgraph.store.base import BaseStore, IndexConfig
from langgraph.store.redis import RedisStore


REDIS_URI = os.environ.get("REDIS_URI", "redis://localhost:6379")
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "text-embedding-3-small")
CHAT_MODEL = os.environ.get("CHAT_MODEL", "gpt-4o")


def _set_env(var: str) -> None:
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


def build_redis_store() -> RedisStore:
    index_config: IndexConfig = {
        "dims": 1536,
        "embed": OpenAIEmbeddings(model=EMBEDDING_MODEL),
        "ann_index_config": {"vector_type": "vector"},
        "distance_type": "cosine",
    }
    with RedisStore.from_conn_string(REDIS_URI, index=index_config) as store:
        store.setup()
        return store


def build_graph(store: BaseStore):
    model = ChatOpenAI(model=CHAT_MODEL, temperature=0)

    def call_model(
        state: MessagesState,
        config: RunnableConfig,
        *,
        store: BaseStore,
    ):
        user_id = config["configurable"]["user_id"]
        namespace = ("memories", user_id)
        memories = store.search(namespace, query=str(state["messages"][-1].content))
        info = "\n".join([d.value["data"] for d in memories])
        system_msg = (
            "You are a helpful assistant talking to the user. "
            f"User info: {info}"
        )

        last_message = state["messages"][-1]
        if "remember" in last_message.content.lower():
            memory = "User name is Bob"
            store.put(namespace, str(uuid.uuid4()), {"data": memory})

        response = model.invoke(
            [{"role": "system", "content": system_msg}] + state["messages"]
        )
        return {"messages": response}

    builder = StateGraph(MessagesState)
    builder.add_node("call_model", call_model)
    builder.add_edge(START, "call_model")

    with RedisSaver.from_conn_string(REDIS_URI) as checkpointer:
        checkpointer.setup()
        return builder.compile(checkpointer=checkpointer, store=store)


def print_stream(stream: Iterable[dict]) -> None:
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()


def demo(graph) -> None:
    config = {"configurable": {"thread_id": "1", "user_id": "1"}}
    input_message = {"role": "user", "content": "Hi! Remember: my name is Bob"}
    print_stream(graph.stream({"messages": [input_message]}, config, stream_mode="values"))

    config = {"configurable": {"thread_id": "2", "user_id": "1"}}
    input_message = {"role": "user", "content": "what is my name?"}
    print_stream(graph.stream({"messages": [input_message]}, config, stream_mode="values"))

    config = {"configurable": {"thread_id": "3", "user_id": "2"}}
    input_message = {"role": "user", "content": "what is my name?"}
    print_stream(graph.stream({"messages": [input_message]}, config, stream_mode="values"))


if __name__ == "__main__":
    _set_env("OPENAI_API_KEY")
    redis_store = build_redis_store()
    graph = build_graph(redis_store)
    demo(graph)

    # Optional: inspect Redis store contents
    # for memory in redis_store.search(("memories", "1")):
    #     print(memory.value)
