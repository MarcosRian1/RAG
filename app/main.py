from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.rag import ask_rag

app = FastAPI()

class Question(BaseModel):
    question: str
    chat_history: list[tuple[str, str]] = Field(default_factory=list)

@app.post('/pergunta')
def ask_question(data: Question):
    answer = ask_rag(data.question, chat_history=data.chat_history)

    return{'answer': answer}