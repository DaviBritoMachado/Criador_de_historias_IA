import streamlit as st
import google.generativeai as genai

api_key = st.secrets['API_KEY']
genai.configure(api_key = api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="HistoryStarter", page_icon="🚀")

st.title("Crie sua história com o HistoryStarter")

st.header("Tente agora!")

nome = st.text_input("Digite o nome do protagonista:")
genero = st.selectbox("Escolha um gênero literário:", ["Fantasia", "Ficção ciêntifica", "Mistério", "Aventura"])
local = st.radio("Escolha um local inicial:", ["Floresta anciente", "Cidade futurista", "Castelo assombrado"])
frase_efeito = st.text_area("Adicione uma frase de efeito ou desafio inicial:")

if st.button("Gerar Início da História"):
    if nome:
        if frase_efeito:
            with st.spinner("Gerando resposta..."):
                resposta = model.generate_content("Crie o início de uma história de " + genero + " com o protagonista chamado " + nome + ". A história começa em " + local + ". Incorpore a seguinte frase ou desafio no início: " + frase_efeito + " com um limite de dois parágrafos.")
                st.write("**Resposta:**")
                st.write(resposta.text)
        else:
            st.warning("Por favor, digite uma frase de efeitou ou desafio inicial.")
    else:
        st.warning("Por favor, digite um nome.")
