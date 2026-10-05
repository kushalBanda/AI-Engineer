import uuid
from functools import lru_cache
from fastapi import APIRouter, HTTPException

from .config import settings
from .schemas import IngestRequest, IngestResponse, QueryRequest, QueryResponse
from .services.embeddings import OpenAIEmbedder
from .services.llm import OpenAILLM
from .services.retrieval import build_prompt, sources_to_schema
from .services.store import DocumentStore, StoredDocument
from .utils.text import chunk_text

router = APIRouter()


@lru_cache(maxsize=1)
def _get_embedder() -> OpenAIEmbedder:
    return OpenAIEmbedder(settings.openai_api_key, settings.openai_embedding_model)


@lru_cache(maxsize=1)
def _get_llm() -> OpenAILLM:
    return OpenAILLM(settings.openai_api_key, settings.openai_llm_model)


@lru_cache(maxsize=1)
def _get_store() -> DocumentStore:
    return DocumentStore(settings.rag_data_path)


@router.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@router.post("/ingest", response_model=IngestResponse)
async def ingest(request: IngestRequest) -> IngestResponse:
    embedder = _get_embedder()
    store = _get_store()

    texts = []
    metadata_list = []
    ids = []
    for doc in request.documents:
        doc_id = doc.id or str(uuid.uuid4())
        if request.chunk_size:
            chunks = chunk_text(doc.text, request.chunk_size)
            for idx, chunk in enumerate(chunks):
                texts.append(chunk)
                metadata_list.append({**doc.metadata, "chunk": idx, "parent_id": doc_id})
                ids.append(f"{doc_id}:{idx}")
        else:
            texts.append(doc.text)
            metadata_list.append(doc.metadata)
            ids.append(doc_id)

    embeddings = embedder.embed(texts)
    if len(embeddings) != len(texts):
        raise HTTPException(status_code=500, detail="Embedding count mismatch")

    stored = [
        StoredDocument(id=doc_id, text=text, metadata=meta, embedding=embedding)
        for doc_id, text, meta, embedding in zip(ids, texts, metadata_list, embeddings)
    ]
    count = await store.add_documents(stored)
    return IngestResponse(stored=count)


@router.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest) -> QueryResponse:
    embedder = _get_embedder()
    llm = _get_llm()
    store = _get_store()

    query_embedding = embedder.embed([request.query])[0]
    top_k = request.top_k or settings.rag_top_k
    max_chars = request.max_context_chars or settings.rag_max_context_chars
    sources = store.search(query_embedding, top_k=top_k)

    prompt = build_prompt(request.query, sources, max_chars)
    answer = llm.generate(prompt)
    return QueryResponse(answer=answer, sources=sources_to_schema(sources))
