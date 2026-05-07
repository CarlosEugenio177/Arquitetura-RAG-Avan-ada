from __future__ import annotations

import os


TERM_MAP = {
    "dor de cabeça": "cefaleia",
    "latejante": "pulsátil",
    "luz incomodando": "fotofobia",
    "enjoo": "náuseas",
    "vomitando": "vômitos",
    "falta de ar": "dispneia",
    "chiado": "sibilância",
    "pressão alta": "hipertensão arterial",
    "coração acelerado": "taquicardia",
    "xixi ardendo": "disúria",
    "urinar toda hora": "polaciúria",
    "dor no peito": "dor torácica",
    "desmaio": "síncope",
    "tontura": "vertigem",
}


def generate_hypothetical_document_rules(query: str) -> str:
    normalized_query = query.lower()
    technical_terms = [
        technical
        for colloquial, technical in TERM_MAP.items()
        if colloquial in normalized_query
    ]

    if not technical_terms:
        technical_terms = ["sintomas inespecíficos", "avaliação clínica"]

    terms_text = ", ".join(dict.fromkeys(technical_terms))
    return (
        "Paciente apresenta quadro clínico descrito em linguagem técnica como "
        f"{terms_text}. Recomenda-se correlacionar os achados com fragmentos "
        "de manual que descrevam sintomas associados, diagnósticos diferenciais "
        "e sinais de alarme."
    )


def generate_hypothetical_document_llm(query: str) -> str | None:
    if os.getenv("USE_LLM_HYDE") != "1" or not os.getenv("OPENAI_API_KEY"):
        return None

    try:
        from openai import OpenAI
    except ImportError:
        return None

    client = OpenAI()
    prompt = (
        "Transforme a query coloquial abaixo em um documento hipotético técnico, "
        "curto, em português, usando jargões médicos. Não dê orientação médica; "
        "apenas descreva sintomas em linguagem de manual.\n\n"
        f"Query: {query}"
    )

    try:
        response = client.responses.create(
            model=os.getenv("OPENAI_HYDE_MODEL", "gpt-4.1-mini"),
            input=prompt,
        )
    except Exception:
        return None

    text = getattr(response, "output_text", "").strip()
    return text or None


def generate_hypothetical_document(query: str) -> str:
    return generate_hypothetical_document_llm(query) or generate_hypothetical_document_rules(query)
