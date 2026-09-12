from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker

#String de conexao com o postegresql local
DATABASE_URL = "postgresql://admin:admin@localhost:5432/agente_rh"

#Cria "motor" de conexao
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Define a tabela onde vmaos salvar as conversas
class Mensagem(Base):
	__tablename__ = "mensagens_chat"

	id = Column(Integer, primary_key=True, index=True)
	id_usuario = Column(Integer, index=True)
	pergunta = Column(Text, nullable=False)
	resposta = Column(Text, nullable=False)

#Esse comando cria a tabela no banco automaticamente se ela não existir
Base.metadata.create_all(bind=engine)
