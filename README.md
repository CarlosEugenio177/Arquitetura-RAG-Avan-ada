# LABORATÓRIO 09: Arquitetura RAG Avançada

Pipeline didático de Retrieval-Augmented Generation (RAG) com HNSW, HyDE e Cross-Encoder, usando dados médicos fictícios.

> Aviso: todos os fragmentos deste projeto são simulados para fins acadêmicos. Eles não devem ser usados como orientação médica real.

## Como instalar

Requisitos: Python 3.10 ou superior.

```bash
pip install -r requirements.txt
```

## Como executar

```bash
python src/main.py
```

A execução usa a query de teste:

```text
dor de cabeça latejante e luz incomodando
```

O console exibirá:

- query original;
- documento hipotético gerado pelo HyDE;
- Top-10 recuperados pelo índice HNSW;
- scores de similaridade;
- Top-3 finais após re-ranking com Cross-Encoder.

## Pipeline

Fluxo implementado:

```text
Query original -> HyDE -> Embedding -> HNSW -> Top-10 -> Cross-Encoder -> Top-3
```

1. A query coloquial do usuário é transformada em um documento hipotético técnico com HyDE.
2. O documento HyDE é vetorizado com `sentence-transformers/all-MiniLM-L6-v2`.
3. Os vetores são normalizados, permitindo usar produto interno como aproximação de similaridade de cosseno.
4. O FAISS `IndexHNSWFlat` recupera rapidamente os 10 documentos mais próximos.
5. O `cross-encoder/ms-marco-MiniLM-L-6-v2` reavalia os pares `[query original, documento]`.
6. Os 3 documentos com maior score do Cross-Encoder são selecionados como contexto final.

## HyDE

O projeto traz duas opções:

- `generate_hypothetical_document_rules`: modo simples, sem API, baseado em regras e dicionário de termos coloquiais para jargões médicos.
- `generate_hypothetical_document_llm`: modo opcional preparado para LLM, caso uma chave de API seja configurada.

Para tentar usar o modo LLM opcional, configure:

```bash
set OPENAI_API_KEY=sua_chave
set USE_LLM_HYDE=1
```

Se a biblioteca `openai` não estiver instalada ou a chamada falhar, o código volta automaticamente para o modo por regras.

## HNSW: M, efConstruction, RAM e qualidade

O HNSW cria um grafo hierárquico de vizinhos aproximados. Em vez de comparar a query com todos os documentos, como em uma busca KNN exata, ele navega pelo grafo para encontrar bons candidatos com menor custo de consulta.

O parâmetro `M` controla aproximadamente quantos vizinhos cada nó mantém no grafo. Valores maiores de `M` aumentam a conectividade, melhoram a chance de recuperar vizinhos relevantes e elevam a qualidade da busca, mas também aumentam o consumo de RAM porque mais arestas precisam ser armazenadas.

O parâmetro `efConstruction` controla o tamanho da lista dinâmica usada durante a construção do índice. Valores maiores deixam a indexação mais lenta e podem consumir mais memória temporária durante a criação do grafo, mas geralmente produzem uma estrutura de melhor qualidade, com caminhos mais úteis para recuperação.

Comparação com KNN exato:

- KNN exato precisa calcular a distância da query contra todos os vetores da base. Ele tende a ter maior precisão, mas o custo de consulta cresce linearmente com o número de documentos.
- HNSW armazena estrutura extra em RAM, principalmente as conexões do grafo, então pode usar mais memória que uma matriz simples de vetores.
- Em troca desse custo extra de memória, HNSW reduz muito o tempo de busca em bases grandes, mantendo boa qualidade aproximada quando `M`, `efConstruction` e `efSearch` são bem ajustados.

Neste laboratório, a base tem apenas 20 documentos, então o ganho de velocidade não é essencial. O objetivo é demonstrar a arquitetura usada em cenários de produção com bases maiores.

## Integridade acadêmica

Partes deste laboratório foram geradas/complementadas com IA, revisadas e validadas por Carlos Eugênio


## Tag/release v1.0

Após revisar, testar e subir o projeto para o GitHub, crie a tag exigida:


