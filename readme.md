# Tech Challenge - Fase 1

Repositório estruturado para o Tech Challenge, compreendendo um ciclo completo de Engenharia de Machine Learning: desde a exploração inicial de dados e construção de modelos preditivos até a criação de uma API REST de alta performance, validada por contratos de dados e testes automatizados.

## 👥 Autoria 
* **Desenvolvedor:** Matheus Brito 


## 🛠️ Tecnologias Utilizadas
* **Python 3.14**
* **Pandas & Scikit-Learn** (Manipulação de dados e Modelagem)
* **FastAPI & Uvicorn** (Construção do serviço web e servidor ASGI)
* **Pydantic** (Validação estrita e contrato de dados)
* **Pytest & HTTPX** (Testes automatizados unitários e de integração)
* **Joblib** (Serialização e persistência de artefatos)

```text
📁 projeto-techchallenge-f1/
├── 📁 data/
│   └── 📄 Telco_Customer_Churn.csv # Dataset original utilizado na EDA e treino (opcional para rodar a API)
├── 📁 docs/
│   ├── 📄 ml_canvas.md              # Entendimento de negócio e métricas
│   ├── 📄 MODEL_CARD.md             # Documentação de performance e vieses
│   └── 📄 tracking_experimentos.csv # Tabela comparativa de modelos (Baseline, Árvore, MLP)
├── 📁 models/
│   ├── 📄 champion_model.pkl        # Modelo preditivo vencedor
│   └── 📄 scaler.pkl                # Padronizador de variáveis numéricas
├── 📁 notebooks/
│   └── 📄 analise_dados_EDA.ipynb   # Notebook de EDA e treinamento inicial
├── 📁 src/
│   ├── 📄 __init__.py               # Módulo de inicialização Python
│   ├── 📄 app.py                    # Servidor da API (FastAPI)
│   └── 📄 predict.py                # Classe de inferência e aplicação do scaler
├── 📁 tests/
│   ├── 📄 __init__.py               # Módulo de testes Python
│   └── 📄 test_app.py               # Testes automatizados com Pytest
├── 📄 .gitignore
├── 📄 requirements.txt              # Dependências congeladas do projeto
└── 📄 README.md                     # Manual de instruções
```

--Obtenção do Dataset (Dados)
Para projetos acadêmicos e portfólios, é comum isolar os dados brutos. Embora a API em produção funcione de forma autônoma utilizando apenas os arquivos binários salvos na pasta models/, o arquivo CSV é necessário caso você deseje reexecutar a Análise Exploratória de Dados (EDA) ou retreinar o modelo no Jupyter Notebook.

Baixe o arquivo de dados: Obtenha a base de dados de Churn de Telecom (como o clássico Telco Customer Churn disponível no Kaggle).
LINK DO CSV:
https://storage.googleapis.com/kaggle-data-sets/6845450/10996893/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20260828%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260828T000009Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=0f4218200be68d15ff27e797d1e6fc9d4041be75b4e22d9c1cae73a6607a7f6b895cf8e90db5b6001fbfc087b8d36e06e7a7b9ea719f42dd5e14b7a1651234dca4625f1798d7b0c99317dfdf8be3e3bfd7ed63ac23cb01492a534d0cd38e15ebab5ed0fd654f484af89c34c03333abce2e03f4b50a78bc81441560b67c0461f5c5036fa721bb90b1081c1b1f53c4bb4c22cf83eea6821000d18a0e8d754cf4c64f9ceb39f3fbe92f28cd2dc1804502efb4bd3cdf4188faca70125e5d03ae0b255b69204d159a18615373bd38e9fd6d1739316b84b30b5dd29e0b739dd27850695904344d7cf262bc56f08501e5e945e340f1cb3fe0d5c92810b1c14567280a33

Organize o diretório: Crie uma pasta chamada data/ na raiz do projeto (caso ela não exista) e coloque o arquivo CSV lá dentro com o nome padronizado (ex: Telco_Customer_Churn.csv).
Nota: Como arquivos de dados brutos costumam ser pesados e dados sensíveis ou públicos de grande volume geralmente ficam fora do controle de versão corporativo, a pasta data/ encontra-se mapeada no .gitignore para não inflar o repositório do Git.

--Como Executar o Projeto Localmente
1. Clonar o repositório e configurar o ambiente virtual
Abra o terminal na pasta de sua preferência e execute os comandos abaixo:

Bash
git clone <url-do-seu-repositorio>
cd projeto-techchallenge-f1

# Criar o ambiente virtual isolado
python -m venv venv

# Ativar o ambiente virtual (No Windows)
venv\Scripts\activate

# Ativar o ambiente virtual (No Mac/Linux)
source venv/bin/activate
2. Instalar as dependências
Com o ambiente virtual ativado, instale os pacotes necessários listados no gerenciador de versões:

Bash
pip install -r requirements.txt
3. Rodar os Testes Automatizados (Pytest)
Para certificar-se de que a aplicação está íntegra, com as rotas operacionais e o contrato de dados blindado, execute o robô de testes:

Bash
python -m pytest
4. Subir a API de Inferência
Inicie o servidor localmente com recarregamento automático ativado:

Bash
uvicorn src.app:app --reload
A API estará escutando em: http://127.0.0.1:8000

📖 Documentação Interativa (Swagger UI)
Com o servidor rodando em segundo plano, você pode interagir visualmente com a API e realizar testes manuais de sucesso e de falha:

Interface Swagger: http://127.0.0.1:8000/docs

Verificação de Saúde (Health Check): http://127.0.0.1:8000/health