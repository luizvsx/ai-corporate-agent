# Corporate AI Agent

Sistema baseado na arquitetura RAG (Retrieval-Augmented Generation) para processamento e consulta de manuais corporativos e políticas de Recursos Humanos. 

O projeto implementa uma pipeline de processamento de linguagem natural (NLP) para buscar contextos semanticamente relevantes em documentos institucionais não-estruturados (PDFs) e fornecer base contextual para respostas automatizadas via LLM.

## Arquitetura e Stack Tecnológico

- **Linguagem:** Python
- **API e Backend:** FastAPI, SQLAlchemy
- **Banco de Dados Relacional:** PostgreSQL (persistência de histórico e sessões)
- **Banco de Dados Vetorial:** Qdrant (armazenamento e busca de embeddings)
- **Orquestração e Processamento:** LangChain, HuggingFace, PyPDF
- **Modelo de Embeddings:** `paraphrase-multilingual-MiniLM-L12-v2` (otimizado para PT-BR)
- **Infraestrutura:** Docker

## Estado do Projeto

Funcionalidades concluídas nas etapas iniciais de desenvolvimento:
- [x] Configuração da infraestrutura via Docker (PostgreSQL e Qdrant).
- [x] Construção da API REST e mapeamento ORM (SQLAlchemy).
- [x] Pipeline de extração e chunking adaptativo de arquivos PDF.
- [x] Geração e ingestão de vetores de alta dimensionalidade.
- [x] Motor de recuperação vetorial via busca semântica.
- [ ] Integração com modelo de linguagem (LLM) para geração de respostas estruturadas.

## Execução Local

### 1. Serviços de Infraestrutura (Docker)

```bash
# Inicializa o banco relacional
docker run --name postgres-agente -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=agente_rh -p 5432:5432 -d postgres:16

# Inicializa o banco vetorial
docker run --name qdrant-agente -p 6333:6333 -d qdrant/qdrant
