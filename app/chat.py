import streamlit as st
import requests

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if not st.session_state.chat_history:
    st.session_state.chat_history.append(('assistant',
        '''
        Olá, eu sou seu assistente especialista em Economia.

        Posso responder perguntas relacionadas a:
        - Taxa de juros nominal e taxa de juros real
        - Capitalização simples versus capitalização composta
        - Taxa de juros equivalentes versus taxa de juros proporcional
        - Índice de referência (benchmark) aplicado a produtos de investimento: conceito e finalidade
        - Volatilidade
        - Prazo médio ponderado de uma carteira de títulos: conceito e riscos associados

        Sobre qual assunto você gostaria de saber?
        '''
    ))

user_message = st.chat_input('Escreva sua mensagem...')

for role, message in st.session_state.chat_history:
    st.chat_message(role).write(message)

if user_message:
    st.chat_message('user').write(user_message)
    st.session_state.chat_history.append(('user', user_message))

    with st.spinner('Digitando...'):
        response = requests.post(
            'http://localhost:8000/pergunta',
            json={'question': user_message},
            timeout=500
        )

        if response.ok:
            answer = response.json()['answer']
            st.chat_message('assistant').write(answer)
            st.session_state.chat_history.append(('assistant', answer))
        else:
            st.error('Erro ao consultar a API.')