from __future__ import annotations

from sentence_transformers import CrossEncoder

from data import Document
from device import select_torch_device


CROSS_ENCODER_MODEL_NAME = "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"
BI_ENCODER_WEIGHT = 0.65
CROSS_ENCODER_WEIGHT = 0.35


def load_cross_encoder() -> CrossEncoder:
    return CrossEncoder(CROSS_ENCODER_MODEL_NAME, device=select_torch_device())


def rerank_documents(
    cross_encoder: CrossEncoder,
    query: str,
    candidates: list[tuple[Document, float]],
) -> list[tuple[Document, float, float, float]]:
    pairs = [[query, document.text] for document, _ in candidates]
    cross_scores = cross_encoder.predict(pairs)
    cross_scores_float = [float(score) for score in cross_scores]
    bi_scores = [float(score) for _, score in candidates]

    normalized_cross_scores = normalize_scores(cross_scores_float)
    normalized_bi_scores = normalize_scores(bi_scores)

    reranked = [
        (
            document,
            cross_score,
            bi_encoder_score,
            (BI_ENCODER_WEIGHT * bi_score) + (CROSS_ENCODER_WEIGHT * cross_score_normalized),
        )
        for (document, bi_encoder_score), cross_score, bi_score, cross_score_normalized in zip(
            candidates,
            cross_scores_float,
            normalized_bi_scores,
            normalized_cross_scores,
            strict=True,
        )
    ]
    return sorted(reranked, key=lambda item: item[3], reverse=True)


def normalize_scores(scores: list[float]) -> list[float]:
    if not scores:
        return []

    min_score = min(scores)
    max_score = max(scores)
    if min_score == max_score:
        return [1.0 for _ in scores]

    return [(score - min_score) / (max_score - min_score) for score in scores]
