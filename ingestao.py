from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from processador_pdf import processar_documento

# 1. Extrair os chunks reaproveitando a sua função modular
caminho_pdf = "documentos/manual_rh.pdf" # Coloque o nome exato do seu arquivo
pedacos = processar_documento(caminho_pdf)

print("\nCarregando o modelo de IA para Embeddings (isso pode demorar um pouquinho na primeira vez)...")

# Usamos o all-MiniLM-L6-v2: é o padrão da indústria para testes rápidos, leve e eficiente.
# 1. Troque o nome do modelo para o multilíngue
modelo_embeddings = HuggingFaceEmbeddings(model_name="paraphrase-multilingual-MiniLM-L12-v2")

# ... (resto do código continua igual até a hora de salvar) ...

# 2. Troque o nome da collection para criar uma nova no banco
QdrantVectorStore.from_texts(
    texts=pedacos,
    embedding=modelo_embeddings,
    url="http://localhost:6333",
    collection_name="manual_rh_pt_collection" # <--- NOME NOVO AQUI
)
print("🎉 Sucesso! Conhecimento injetado no Qdrant com sucesso!")
