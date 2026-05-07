# Resultados dos Testes

Este arquivo registra os testes manuais executados no projeto de Arquitetura RAG Avancada.

## Ambiente

- Sistema: Windows
- Ambiente Python: `.venv`
- Indice vetorial: FAISS `IndexHNSWFlat` via `faiss-cpu`

## Query de Teste

```text
dor de cabeca latejante e luz incomodando
```

## Documento HyDE Gerado

```text
Paciente apresenta quadro clinico descrito em linguagem tecnica como cefaleia, pulsatil, fotofobia. Recomenda-se correlacionar os achados com fragmentos de manual que descrevam sintomas associados, diagnosticos diferenciais e sinais de alarme.
```

O HyDE converteu a query coloquial em termos tecnicos relevantes:

- `dor de cabeca` -> `cefaleia`
- `latejante` -> `pulsatil`
- `luz incomodando` -> `fotofobia`

## Resultado do HNSW/Bi-Encoder

Modelo de embeddings:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Top-10 recuperados:

| Posicao | Documento | Score aproximado |
|---:|---|---:|
| 1 | DOC-001 - Enxaqueca com aura | 0.6265 |
| 2 | DOC-016 - Meningite | 0.4708 |
| 3 | DOC-021 - Vertigem vestibular | 0.4303 |
| 4 | DOC-012 - Hipoglicemia | 0.4246 |
| 5 | DOC-013 - Sindrome coronariana aguda | 0.4025 |
| 6 | DOC-014 - Insuficiencia cardiaca | 0.4017 |
| 7 | DOC-004 - Asma bronquica | 0.3926 |
| 8 | DOC-010 - Pielonefrite | 0.3917 |
| 9 | DOC-015 - Acidente vascular cerebral | 0.3880 |
| 10 | DOC-002 - Crise hipertensiva | 0.3638 |

Conclusao parcial: o funil amplo com HNSW/Bi-Encoder funcionou bem, pois recuperou `DOC-001 - Enxaqueca com aura` em primeiro lugar para uma query sobre cefaleia pulsatil e fotofobia.

## Teste com Cross-Encoder Isolado

Modelo inicial:

```text
cross-encoder/ms-marco-MiniLM-L-6-v2
```

Top-3 obtido:

| Posicao | Documento | Score Cross-Encoder | Score Bi-Encoder |
|---:|---|---:|---:|
| 1 | DOC-013 - Sindrome coronariana aguda | -9.2940 | 0.4025 |
| 2 | DOC-010 - Pielonefrite | -9.8584 | 0.3917 |
| 3 | DOC-002 - Crise hipertensiva | -10.0417 | 0.3638 |

Esse resultado foi considerado semanticamente ruim, porque documentos menos relacionados foram promovidos acima de `DOC-001 - Enxaqueca com aura`.

## Teste com Cross-Encoder Multilingual

Modelo ajustado:

```text
cross-encoder/mmarco-mMiniLMv2-L12-H384-v1
```

Top-3 obtido usando apenas o score do Cross-Encoder:

| Posicao | Documento | Score Cross-Encoder | Score Bi-Encoder |
|---:|---|---:|---:|
| 1 | DOC-013 - Sindrome coronariana aguda | -4.7449 | 0.4025 |
| 2 | DOC-012 - Hipoglicemia | -4.7502 | 0.4246 |
| 3 | DOC-001 - Enxaqueca com aura | -4.7942 | 0.6265 |

Apesar de usar um modelo multilingual, o Cross-Encoder isolado ainda nao colocou o documento mais relevante no topo.

## Resultado Final com Ranking Hibrido

Foi adotado um score final hibrido combinando:

- score normalizado do Bi-Encoder/HNSW
- score normalizado do Cross-Encoder

Pesos usados:

```text
Bi-Encoder: 0.65
Cross-Encoder: 0.35
```

Top-3 final:

| Posicao | Documento | Score final hibrido | Score Cross-Encoder | Score Bi-Encoder |
|---:|---|---:|---:|---:|
| 1 | DOC-001 - Enxaqueca com aura | 0.9920 | -4.7942 | 0.6265 |
| 2 | DOC-016 - Meningite | 0.5186 | -5.3385 | 0.4708 |
| 3 | DOC-012 - Hipoglicemia | 0.4995 | -4.7502 | 0.4246 |

## Conclusao

O laboratorio foi validado de ponta a ponta:

- HyDE transformou a query coloquial em linguagem tecnica.
- HNSW recuperou corretamente o documento mais relevante no primeiro lugar.
- O Cross-Encoder isolado apresentou instabilidade semantica para a query curta em portugues.
- O ranking hibrido corrigiu o resultado final e colocou `DOC-001 - Enxaqueca com aura` no Top-1.

Aprendizado principal: em pipelines RAG, nao basta o codigo executar. E necessario validar semanticamente os resultados de cada etapa e combinar sinais quando um unico modelo nao produz o ranking esperado.
