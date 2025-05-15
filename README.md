<div align="center">
<h1><div>👾 Hackathon-1.25 IDP 👾</div></h1>

<h3><a href="https://docs.google.com/document/d/1N_YBdELL-t24lyyPf8wAWqKgzYzSLLxKORNxS0-Hn6A/edit?usp=sharing">Documentação</a></h3>

<h1><div>Sharebite</div></h1>

<img src="frontend/SharebiteNtext.png" width="40%" />
</div>

Sistema desenvolvido durante a 5ª edição do Hackathon do IDP em apenas 20h com foco em **reduzir o desperdício de alimentos** e **conectar empresas doadoras com pessoas em vulnerabilidade**, respeitando as normas da ANVISA. A aplicação permite validar alimentos, gerar relatórios interativos e integrar incentivos sociais e fiscais, tudo com **suporte de IA** que age como um agente inspetor da ANVISA e valida se os alimentos estão próprios para consumo ou não.

<div align="center">
<h2> 🐍 Ferramentas e Linguagens Utilizadas </h2>
<img src="https://skillicons.dev/icons?i=py,docker,mongodb,linux,powershell,vim,flask" />
</div>

<h2 align="center">Descrição do Projeto</h2>

A plataforma opera com três módulos principais:

- **Interface Web (Streamlit):** onde usuários registram e acompanham doações.
- **Backend Flask (API):** que realiza a lógica de validação e processamento.
- **Banco de dados MongoDB:** armazena alimentos, doações, empresas e registros históricos.

O sistema também se destaca por:

- **Validação automática** dos alimentos com base em critérios da ANVISA.
- **Relatórios** com gráficos interativos sobre desempenho e impacto social.
- **Proposta** de integração com o programa **Nota Legal (DF)** para gerar incentivos fiscais a empresas doadoras.
- **Uso de IA** (Gemini API) para análises e suporte à tomada de decisão.

## ✅ O que foi Desenvolvido

- [X] Interface de formulário para empresas e dashboard com Streamlit.
- [X] Relatórios com dados de doações, rejeições e excedente.
- [X] Integração com modelo de IA para auxiliar inspeção e triagem.
- [X] Sistema dockerizado para facilitar deploy e execução local.

---

## 🗂️ Estrutura do Projeto
```PY
Hackathon-1.25/
├── app/ # Backend Flask (API)
│ └── app.py
│ └── validator
│   └── engine.py
│   └── rules.yaml
├── database/ # Dados de exemplo (.csv)
│ └── Produtos.csv
│ └── Empresas.csv
│ └── Validacao.csv
├── frontend/ # Frontend com Streamlit
│ └── home.py

├── gemini/ # Integração com IA (Google Gemini)
│ └── gemini_chat.py
├── .env # Exemplo de variável de ambiente
├── Dockerfile # Dockerfile da API Flask
├── docker-compose.yml # Orquestração dos serviços
└── requirements.txt # Dependências Python
```

## 🧪 Como Executar o Projeto

> Pré-requisitos: Docker, Docker Compose, GitHub e conexão com a internet.

### 1. Clone o repositório

```bash
git clone https://github.com/Felipebc2/Hackathon-1.25.git
cd Hackathon-1.25
```

### 2. GEMINI_API_KEY

```bash
echo "GEMINI_API_KEY=sua-api-key" > .env
```

- Para obter a chave, Acesse o link https://aistudio.google.com/app/apikey e faça login com sua conta google. No canto superior direito da tela clique no botão "Criar chave de API", Após isso crie um arquivo .env com a chave de API gerada pelo gemini.

### 3. Subir os container com Docker

```bash
docker compose up -d --build
```

- Caso algum requerimento esteja faltando instale com ```pip install -r requeriments.txt``` ou ```pip install X```, trocando o X pelo requerimento faltante.

#### Requerimentos
```bash
flask
streamlit
requests
pymongo
pyyaml
google-generativeai
python-dotenv
matplotlib
```

### 4. Execute o Streamlit
```bash
streamlit run ./frontend/home.py
```

- Se estiver dentro da pasta do front end apenas rode
```bash
streamlit run home.py
```

## Observações
- A IA utilizada pode ser trocada ou expandida para novos modelos via Gemini.
- O sistema aceita expansão para novos critérios sanitários da ANVISA.
- Funcionalidade de login, controle de acesso, permissões, leitura de imagens, prompt interagível e troca de Streamlit para outro Frontend serão adicionados no futuro.

## Equipe
- Felipe Castro
    - Dev Full Stack
    - Integração Software-IA
- Fábio Luis de Carvalho Terra
    - Dev Front End
    - Database Administrator
- Sara Pacheco de Azevedo
    - Product Owner
    - Scrum Master
- Pietro Branco
    - Integração Software-IA
    - Requirements Analyst

---

Este projeto está licenciado sob a MIT License.

<<<<<<< HEAD
© 2024 Felipe Castro, Fábio Terra, Sara Azevedo, Pietro Branco. Todos os direitos reservados.
=======
© 2024 Felipe Castro, Fábio Terra, Sara Azevedo, Pietro Branco. Todos os direitos reservados.
>>>>>>> 9b5fd995daa27bdeaafdd04d546fcf989f2dd3ca
