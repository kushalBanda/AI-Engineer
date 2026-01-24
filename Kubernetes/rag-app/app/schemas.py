from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class DocumentIn(BaseModel):
    id: Optional[str] = None
    text: str = Field(..., min_length=1)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class IngestRequest(BaseModel):
    documents: List[DocumentIn]
    chunk_size: Optional[int] = Field(default=None, ge=200)


class IngestResponse(BaseModel):
    stored: int


class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1)
    top_k: Optional[int] = Field(default=None, ge=1, le=50)
    max_context_chars: Optional[int] = Field(default=None, ge=500)


class SourceDocument(BaseModel):
    id: str
    text: str
    metadata: Dict[str, Any]
    score: float


class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceDocument]
