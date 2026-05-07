from __future__ import annotations

from data import load_medical_manual_fragments
from device import select_torch_device
from hyde import generate_hypothetical_document
from index import build_hnsw_index, embed_texts, load_embedding_model, search_hnsw
from rerank import load_cross_encoder, rerank_documents


TEST_QUERY = "dor de cabeça latejante e luz incomodando"
TOP_K_RETRIEVE = 10
TOP_K_FINAL = 3


def print_retrieved_documents(results: list[tuple[object, float]]) -> None:
    print("\n=== Top-10 recuperados via HNSW/Bi-Encoder ===")
    for position, (document, score) in enumerate(results, start=1):
        print(f"\n{position}. {document.id} | {document.title}")
        print(f"   score_cosseno_aproximado={score:.4f}")
        print(f"   {document.text}")


def print_final_documents(results: list[tuple[object, float, float, float]]) -> None:
    print("\n=== Top-3 finais após Cross-Encoder ===")
    for position, (document, cross_score, bi_score, final_score) in enumerate(results[:TOP_K_FINAL], start=1):
        print(f"\n{position}. {document.id} | {document.title}")
        print(f"   score_final_hibrido={final_score:.4f}")
        print(f"   score_cross_encoder={cross_score:.4f}")
        print(f"   score_bi_encoder={bi_score:.4f}")
        print(f"   {document.text}")


def main() -> None:
    documents = load_medical_manual_fragments()
    document_texts = [document.text for document in documents]

    print("=== LAB 09: Arquitetura RAG Avançada ===")
    print("Dados simulados para fins acadêmicos; não usar como orientação médica real.")
    print(f"Device PyTorch selecionado: {select_torch_device()}")
    print(f"\nQuery original: {TEST_QUERY}")

    hyde_document = generate_hypothetical_document(TEST_QUERY)
    print(f"\nDocumento HyDE:\n{hyde_document}")

    print("\nCarregando modelo de embeddings...")
    embedding_model = load_embedding_model()
    document_embeddings = embed_texts(embedding_model, document_texts)

    print("Construindo índice FAISS HNSW com M=32, efConstruction=80, efSearch=64...")
    hnsw_index = build_hnsw_index(
        document_embeddings,
        m=32,
        ef_construction=80,
        ef_search=64,
    )

    hyde_embedding = embed_texts(embedding_model, [hyde_document])[0]
    retrieved_documents = search_hnsw(
        hnsw_index,
        hyde_embedding,
        documents,
        top_k=TOP_K_RETRIEVE,
    )
    print_retrieved_documents(retrieved_documents)

    print("\nCarregando Cross-Encoder para re-ranking...")
    cross_encoder = load_cross_encoder()
    reranked_documents = rerank_documents(cross_encoder, TEST_QUERY, retrieved_documents)
    print_final_documents(reranked_documents)


if __name__ == "__main__":
    main()
