from __future__ import annotations

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from data import Document
from device import select_torch_device


EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def load_embedding_model() -> SentenceTransformer:
    return SentenceTransformer(EMBEDDING_MODEL_NAME, device=select_torch_device())


def embed_texts(model: SentenceTransformer, texts: list[str]) -> np.ndarray:
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    )
    return embeddings.astype("float32")


def build_hnsw_index(
    embeddings: np.ndarray,
    m: int = 32,
    ef_construction: int = 80,
    ef_search: int = 64,
) -> faiss.IndexHNSWFlat:
    dimension = embeddings.shape[1]
    index = faiss.IndexHNSWFlat(dimension, m, faiss.METRIC_INNER_PRODUCT)
    index.hnsw.efConstruction = ef_construction
    index.hnsw.efSearch = ef_search
    index.add(embeddings)
    return index


def search_hnsw(
    index: faiss.IndexHNSWFlat,
    query_embedding: np.ndarray,
    documents: list[Document],
    top_k: int = 10,
) -> list[tuple[Document, float]]:
    scores, indices = index.search(query_embedding.reshape(1, -1), top_k)
    results: list[tuple[Document, float]] = []

    for doc_index, score in zip(indices[0], scores[0], strict=True):
        if doc_index == -1:
            continue
        results.append((documents[int(doc_index)], float(score)))

    return results
