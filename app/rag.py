from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google import genai
from google.genai import types
from app.functions import get_secret

api_key = get_secret('API_KEY')

# Instanciando o SDK
client = genai.Client(api_key=api_key)

def ask_rag(question: str):
    embeddings = GoogleGenerativeAIEmbeddings(
        model='gemini-embedding-001',
        google_api_key = get_secret('API_KEY')
    )

    db = Chroma(
        persist_directory = 'chroma',
        embedding_function=embeddings
    )

    docs = db.similarity_search(question, k=3)

    context = '\n\n'.join([doc.page_content for doc in docs])

    prompt = f'''
        Use apenas o contexto abaixo para responder a pergunta.
        Se a resposta não estiver no contexto, diga "Não consegui encontrar a informação nas minhas fontes. Há outro algum outro assunto no qual posso ajudar?".

        Regras:
        - Responda diretamente, sem raciocínio passo a passo.
        - Mantenha uma linguagem simples, clara e um pouco informal.
        - Utilize no máximo 200 palavras, quando suficiente.
        - Não invente informações.
        - Não mencione onde encontrou.

        Contexto:
        {context}

        Pergunta:
        {question}
    '''

    # Configurações da resposta como modelo, contexto e segurança    
    response = client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=prompt,
        config=types.GenerateContentConfig(
            safety_settings = [
                types.SafetySetting(
                category='HARM_CATEGORY_HATE_SPEECH',threshold='BLOCK_ONLY_HIGH'),
            ],
            max_output_tokens=300,
            temperature=1
        )
    )

    return response.text