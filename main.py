from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, Mensagem  # Importando o que criamos no outro arquivo!

app = FastAPI(title="Agente Corporativo API")

# Molde do que o usuário vai enviar
class PerguntaUsuario(BaseModel):
    texto: str
    id_usuario: int = 1

# Função para abrir a conexão com o banco e fechar depois que usar
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, Mundo! Meu servidor back-end está no ar!"}

# Agora a rota recebe o banco de dados (db) como dependência
@app.post("/chat")
def receber_mensagem(pergunta: PerguntaUsuario, db: Session = Depends(get_db)):
    
    # 1. Resposta falsa (até colocarmos a IA)
    resposta_simulada = "Ainda não tenho um cérebro RAG, mas já salvei sua mensagem no banco!"

    # 2. Criando o registro no formato da nossa Tabela
    nova_mensagem = Mensagem(
        id_usuario=pergunta.id_usuario,
        pergunta=pergunta.texto,
        resposta=resposta_simulada
    )
    
    # 3. Adicionando e salvando (commit) no PostgreSQL
    db.add(nova_mensagem)
    db.commit()
    
    # 4. Atualiza o objeto para pegar o ID que o banco gerou automaticamente
    db.refresh(nova_mensagem) 

    # 5. Retorna o sucesso para o front-end
    return {
        "status": "sucesso",
        "id_mensagem": nova_mensagem.id, # O ID real do banco!
        "mensagem_salva": nova_mensagem.pergunta,
        "resposta_bot": nova_mensagem.resposta
    }
