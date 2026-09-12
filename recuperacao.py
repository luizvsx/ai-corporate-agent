from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

# 1. Carregamos o novo modelo Multilíngue
modelo_embeddings = HuggingFaceEmbeddings(model_name="paraphrase-multilingual-MiniLM-L12-v2")

# 2. A LINHA QUE FUGIU: Conectamos ao seu Qdrant que está rodando no Docker
cliente_qdrant = QdrantClient(url="http://localhost:6333")

# 3. Conectamos à coleção NOVA
vector_store = QdrantVectorStore(
    client=cliente_qdrant,
    collection_name="manual_rh_pt_collection",
    embedding=modelo_embeddings
)

# 4. A pergunta do usuário
pergunta = "Quais são as regras e benefícios relacionados a férias?"

print(f"🤖 Realizando busca semântica para a pergunta: '{pergunta}'\n")

# 5. Pedimos os 3 fragmentos de texto (chunks) mais relevantes
resultados = vector_store.similarity_search(pergunta, k=3)

# 6. Exibimos o que a IA achou
for i, documento in enumerate(resultados, 1):
    print(f"--- PEDAÇO ENCONTRADO {i} ---")
    print(documento.page_content)
    print("=" * 60 + "\n")
