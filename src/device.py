from __future__ import annotations

import os

import torch


def select_torch_device() -> str:
    requested_device = os.getenv("RAG_DEVICE", "auto").strip().lower()

    if requested_device in {"cpu", "cuda"}:
        if requested_device == "cuda" and not torch.cuda.is_available():
            print("RAG_DEVICE=cuda solicitado, mas CUDA nao esta disponivel. Usando CPU.")
            return "cpu"
        return requested_device

    return "cuda" if torch.cuda.is_available() else "cpu"
