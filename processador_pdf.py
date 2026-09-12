import os
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Caminho do arquivo (coloque o nome exato do seu PDF aqui)
caminho_pdf = "documentos/manual_rh.pdf"

def processar_documento(caminho):
    print(f"Lendo o arquivo: {caminho}...")
    
    # 2. Extraindo o texto do PDF
    leitor = PdfReader(caminho)
    texto_completo = ""
    
    for pagina in leitor.pages:
        # Extrai o texto de cada página e junta tudo
        texto_da_pagina = pagina.extract_text()
        if texto_da_pagina:
            texto_completo += texto_da_pagina + "\n"
            
    print(f"Sucesso! Extraídos {len(texto_completo)} caracteres do documento.")

    # 3. Estratégia de Chunking (Fatiamento)
    # Por que fatiar? A IA não consegue ler um manual de 100 páginas de uma vez.
    # chunk_size: Pedaços de 1000 caracteres.
    # chunk_overlap: 200 caracteres se repetem entre um pedaço e outro para não cortar uma frase no meio.
    fatiador = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    
    pedacos = fatiador.split_text(texto_completo)
    print(f"O documento foi perfeitamente fatiado em {len(pedacos)} pedaços (chunks).\n")
    
    return pedacos

# 4. Executando o teste isolado
if __name__ == "__main__":
    # Verifica se o arquivo existe antes de rodar
    if not os.path.exists(caminho_pdf):
        print(f"ERRO: O arquivo {caminho_pdf} não foi encontrado!")
    else:
        chunks = processar_documento(caminho_pdf)
        
        # Exibe apenas o primeiro chunk para você ver a mágica acontecendo
        if chunks:
            print("--- VISUALIZAÇÃO DO PRIMEIRO PEDAÇO (CHUNK 1) ---")
            print(chunks[0])
            print("-------------------------------------------------")
