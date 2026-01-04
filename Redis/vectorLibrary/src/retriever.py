from langchain_community.document_loaders import WebBaseLoader

from langchain_redis import RedisVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.tools.retriever import create_retriever_tool

from config.openai import get_embeddings
from config.settings import Settings

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

def get_retriever_tool():
    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=100, chunk_overlap=50
    )
    doc_splits = text_splitter.split_documents(docs_list)

    # Add to document chunks to Redis
    vectorstore = RedisVectorStore.from_documents(
        doc_splits,
        get_embeddings(),
        redis_url=Settings().get_redis_url(),
        index_name="rag-redis",
    )
    # get RedisVectorStore as a retriever
    retriever = vectorstore.as_retriever()

    return create_retriever_tool(
        retriever,
        "retrieve_blog_posts",
        "Search and return information about Lilian Weng blog posts on LLM agents, prompt engineering, and adversarial attacks on LLMs.",
    )


def get_tools():
    return [get_retriever_tool()]
