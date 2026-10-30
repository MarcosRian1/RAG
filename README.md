# 🤖 Chatbot RAG — Assistente de Economia

## 📌 Sobre o projeto

Este projeto consiste no desenvolvimento de um chatbot com Inteligência Artificial, utilizando a arquitetura **RAG (Retrieval-Augmented Generation)**, que combina recuperação de informações com geração de respostas por modelo de linguagem.

O objetivo é permitir que o usuário realize perguntas em linguagem natural sobre **economia**, recebendo respostas fundamentadas em uma base de conhecimento composta por documentos nos formatos **TXT e PDF**.

A aplicação utiliza o modelo **Gemini**, uma API desenvolvida com **FastAPI** e uma interface interativa construída com **Streamlit**.

## 🚀 Funcionalidades

- **Recuperação de informações:** busca de conteúdos relevantes em arquivos TXT e PDF sobre economia.
- **Geração de respostas:** utilização do Gemini para produzir respostas contextualizadas.
- **Histórico de conversas:** manutenção das interações anteriores para melhorar a continuidade do diálogo.
- **Integração via API REST:** comunicação por requisições HTTP POST.
- **Respostas fundamentadas:** geração de respostas com base nas informações recuperadas dos documentos.
- **Tratamento de erros:** gerenciamento de falhas nas requisições e na geração de respostas.
- **Formatação matemática:** suporte à apresentação de fórmulas e cálculos por meio de Markdown e LaTeX.

## 🧠 Arquitetura RAG

O funcionamento da aplicação segue as seguintes etapas:

1. O usuário envia uma pergunta sobre economia pela interface Streamlit.
2. O frontend encaminha a pergunta e o histórico da conversa para a API FastAPI.
3. O sistema recupera informações relevantes dos documentos TXT e PDF.
4. O contexto recuperado é combinado com a pergunta, o histórico da conversa e as instruções do sistema.
5. O modelo Gemini processa as informações e gera uma resposta.
6. A API retorna a resposta ao Streamlit, que a apresenta ao usuário.

## ⚙️ Configurações do assistente

- **Modelo de linguagem:** Gemini.
- **Base de conhecimento:** documentos TXT e PDF sobre economia.
- **Contexto conversacional:** histórico de interações anteriores.
- **Estilo de resposta:** linguagem simples, clara e objetiva.
- **Limite recomendado:** até 200 palavras por resposta, quando suficiente.
- **Restrição de conteúdo:** evitar informações não sustentadas pelo contexto recuperado.
- **Tratamento de informações ausentes:** informar quando não houver informações suficientes nos documentos.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **Gemini API:** geração de respostas por Inteligência Artificial.
- **FastAPI:** desenvolvimento da API REST.
- **Streamlit:** construção da interface de conversação.
- **Pydantic:** validação dos dados recebidos pela API.
- **Requests:** comunicação HTTP entre Streamlit e FastAPI.

## 📂 Organização do projeto

| Arquivo | Responsabilidade |
|---|---|
| `chat.py` | Interface Streamlit e gerenciamento do histórico |
| `main.py` | API FastAPI e rota de recebimento das perguntas |
| `rag.py` | Recuperação de informações dos documentos e geração de respostas |

## 💻 Como executar localmente

**1. Clone o repositório**

```bash
git clone https://github.com/MarcosRian1/RAG.git
```

**2. Acesse a pasta do projeto**

```bash
cd RAG
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente**

Configure a chave de acesso à API do Gemini, conforme disponibilizada pela Google AI Studio.

**5. Realize o processo de ingestão dos documentos**

Considerando que `ingest.py` esteja dentro do pacote `app`:

```bash
python app/ingest.py
```

**6. Inicie a API FastAPI**

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

`http://localhost:8000`

A documentação interativa poderá ser acessada em:

`http://localhost:8000/docs`

**7. Inicie a interface Streamlit**

Em outro terminal, execute:

```bash
python -m streamlit run app/chat.py
```

A interface estará disponível em:

`http://localhost:8501`

## 🔄 Comunicação entre frontend e backend

A comunicação é realizada por meio de requisições HTTP POST para o endpoint:

`POST /pergunta`

Exemplo de requisição:

```json
{
  "question": "Qual é a fórmula dos juros compostos?",
  "chat_history": [
    [
      "user",
      "Explique o conceito de juros compostos."
    ],
    [
      "assistant",
      "Juros compostos são calculados sobre o montante acumulado."
    ]
  ]
}
```

Exemplo de resposta da API:

```json
{
  "answer": "A fórmula do montante é VF = VP × (1 + r)^n."
}
```

## 🎯 Objetivo do projeto

Demonstrar a aplicação prática da arquitetura RAG no desenvolvimento de um assistente inteligente especializado em economia, capaz de recuperar informações relevantes de documentos TXT e PDF, utilizar o contexto conversacional e gerar respostas fundamentadas na base de conhecimento.

O projeto também explora a integração entre modelos de linguagem, recuperação documental, APIs REST e interfaces web desenvolvidas em Python.
