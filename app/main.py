from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.rag import ask_rag

# Criação da API
app = FastAPI()

# Validação dos paramêtros
class Question(BaseModel):
    question: str
    chat_history: list[tuple[str, str]] = Field(default_factory=list)

# Envio da pergunta do usuário
@app.post('/pergunta')
def ask_question(data: Question):
    answer = ask_rag(data.question, chat_history=data.chat_history)

    return{'answer': answer}