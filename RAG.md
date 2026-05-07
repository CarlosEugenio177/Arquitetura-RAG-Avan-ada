LABORATÓRIO 09: Arquitetura RAG Avançada (HNSW, HyDE e
Cross-Encoders)

1. Objetivo do Laboratório
Implementar, em Python, um pipeline de Retrieval-Augmented Generation (RAG)
de nível de produção.
2. Contexto do Problema Vocês devem construir um assistente de busca em manuais médicos privados.
Quando o paciente digita uma query coloquial e vaga (ex: "dor de cabeça
latejante e luz incomodando" ), a Similaridade de Cosseno pura falha, pois o "espaço vetorial das perguntas" é diferente do jargão técnico dos manuais (ex:
"cefaléia pulsátil e fotofobia" ). O sistema de vocês interceptar a pergunta, usar um LLM para gerar uma ponte semântica (HyDE), buscar rapidamente em um grafo hierárquico e refinar a precisão matemática antes de entregar os
documentos à IA geradora.
3. Roteiro de Implementação (Passo a Passo)
Passo 1: Construção e Indexação do Grafo HNSW
● Crie um conjunto de dados simulado contendo pelo menos 20
fragmentos de manuais técnicos (você pode gerar isso com IA, focando
em jargões de TI, Direito ou Saúde).
● Utilize um modelo de Embedding (ex: text-embedding-3-small da OpenAI
ou um modelo BERT da Hugging Face) para converter os 20 textos em vetores densos.
● Inicialize um banco de dados vetorial (como FAISS ou ChromaDB)
configurando explicitamente um índice HNSW.
● Tarefa Analítica: No README.md, explique rapidamente como os
hiperparâmetros de arquitetura do HNSW (M e ef_construction) afetam o
consumo de memória RAM do servidor em comparação a uma busca
K-Nearest Neighbors (KNN) exata.
Passo 2: Query Transformation (A Mágica do HyDE)
● Escreva uma função que receba uma query coloquial do usuário.

● Esta função deve fazer uma chamada ao LLM pedindo para ele alucinar
uma resposta técnica (Documento Hipotético).
● Vetorize este documento falso gerado pelo LLM. Ele servirá como sua
nova âncora geométrica no espaço vetorial.
Passo 3: A Busca Rápida (Retrieve via Bi-Encoder)
● Utilizando o vetor do Passo 2, faça uma busca de Similaridade de
Cosseno no índice HNSW.
● Recupere os Top-10 documentos mais próximos (o "funil largo").
Imprima o resultado desta etapa no console para comprovar a
recuperação rápida.
Passo 4: O Filtro Fino (Re-ranking com Cross-Encoder)
● Importe um modelo Cross-Encoder da biblioteca sentence-transformers
(ex: cross-encoder/ms-marco-MiniLM-L-6-v2).
● Passe a query original unida aos 10 documentos recuperados ([CLS]
Query [SEP] Documento) pelo Cross-Encoder.
● Ordene os 10 documentos com base no novo score de atenção
profunda.
● Imprima os Top-3 documentos finais que sobreviveram ao funil e que
seriam injetados no contexto do LLM.

4. Critérios de Avaliação e Contrato Pedagógico
O laboratório comporá a nota da P2 e seguirá rigorosamente as regras de
integridade do Contrato Pedagógico.
4.1. Formato de Entrega e Versionamento:
● Plataforma: O código-fonte (arquivos .py ou .ipynb) deve ser submetido
obrigatoriamente através de um repositório no GitHub. O link deve ser
postado na plataforma iCEV Digital.
● Versionamento: A versão final a ser corrigida deve conter
obrigatoriamente a tag ou release "v1.0".
4.2. Política de Integridade Acadêmica e Uso de IA:

● Uso Permitido: Vocês podem usar ferramentas de IA generativa para
brainstorming , geração dos textos fictícios da base de dados e templates
de código, seguida de revisão crítica.
● Declaração Obrigatória: É obrigatório inserir no README.md a seguinte
nota: "Partes deste laboratório foram geradas/complementadas com IA,
revisadas e validadas por [Seu Nome]".
● Proibição Severa: Submeter códigos inteiros gerados pela IA sem
entendimento prévio, ou "emprestar" o trabalho de um colega (mesmo
alterando variáveis), configura quebra de contrato. A punição é a nota 0
(zero) na atividade e registro da ocorrência. A reincidência leva à
reprovação imediata.
4.3. Política de Prazos e Atrasos:
● Trabalhos devem ser enviados até as 23h59 da data estipulada.
● 1 dia de atraso: penalidade contratual de -20% na nota.
● De 2 a 3 dias de atraso: penalidade contratual de -50% na nota.
● Mais de 3 dias de atraso: Nota 0 (zero) , exceto mediante atestado ou
justificativa oficial.