import streamlit as st
import os
from dotenv import load_dotenv

# Carregamento da chave da API
def get_secret(key):
    try:
        return st.secrets[key]
    except Exception:
        load_dotenv()
        return os.getenv(key)