import streamlit as st

# Define page layout
st.set_page_config(page_title="App Principal", layout="centered")

# Sidebar setup
with st.sidebar:
    st.title("Navegação do App")
    st.markdown(
        '[![Open in GitHub](https://github.com/codespaces/badge.svg)](https://github.com/Felipebc2/Hackathon-1.25)',
        unsafe_allow_html=True
    )
    st.image("img/SharebiteNtext.png", caption=" ", use_container_width=True)
    
# Main content of the page
st.title("Bem-vindo ao ShareBite!")

# Centraliza a imagem usando columns do Streamlit
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("img/SharebiteNtext.png", caption="", use_container_width=True)
st.markdown("""
    Este aplicativo foi desenvolvido para ajudar na validação de doações de alimentos e na visualização de dados sobre a quantidade de produtos disponíveis para doação.
    
    Navegue usando o menu lateral para acessar as páginas de **Formulário de Viabilidade** ou **Dashboard de Estatísticas**.
            
    **Quando usar o Dashboard?** Use o dashboard quando quiser visualizar os dados dos alimentos que sobraram.
            
    **Quando usar o Formulário?** Use o formulário quando quiser adicionar alimentos ao banco de dados, verficando se ele é validado pela ANVISA.
            
""")