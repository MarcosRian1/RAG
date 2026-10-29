from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from functions import get_secret
import os
import time

DATA_PATH = 'data/docs'
CHROMA_PATH = 'chroma'

def load_documents():
    documents = []

    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)

        if path.endswith('.pdf'):
            loader = PyPDFLoader(path)
        else:
            loader = TextLoader(path)

        documents.extend(loader.load())

    return documents

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 100
    )

    return splitter.split_documents(documents)

def ingest():
    documents = load_documents()
    chunks = split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model = 'gemini-embedding-001',
        google_api_key=get_secret('API_KEY')
    )

    db = Chroma(
        persist_directory = CHROMA_PATH,
        embedding_function=embeddings
    )

    batch_size = 20
    intervalo = 15

    total = len(chunks)

    for inicio in range(0, total, batch_size):
        lote = chunks[inicio:inicio + batch_size]

        db.add_documents(lote)

        processados = min(inicio + batch_size, total)

        print(f"Processados: {processados}/{total}")

        if processados < total:
            time.sleep(intervalo)

    print(f'Ingestão concluída: {len(chunks)} chunks criados.')

if __name__ == '__main__':
    ingest()