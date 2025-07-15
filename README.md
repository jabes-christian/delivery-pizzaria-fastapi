
# 🍕 Delivery Pizzaria API

API REST construída com **Python** e **FastAPI**, projetada para gerenciar pedidos de uma pizzaria. Possui autenticação via JWT, gerenciamento de usuários e pedidos, banco de dados relacional com SQLite e controle de versões usando Alembic.

Status do Projeto: (**Em andamneto**)

---

## 🚀 Tecnologias utilizadas

- **Python** – Linguagem principal
- **FastAPI** – Framework web moderno e rápido
- **SQLAlchemy** – ORM para manipulação do banco
- **Alembic** – Migrações de banco de dados
- **SQLite** – Banco de dados leve e prático
- **Pydantic** – Validação de dados
- **JWT (JSON Web Token)** – Autenticação segura baseada em tokens

---

## 📁 Estrutura do Projeto

```
DELIVERY_PIZZARIA/
│
├── alembic/                # Migrações do banco de dados
├── __pycache__/           # Cache do Python
├── venv/                  # Ambiente virtual
├── auth_routes.py         # Rotas de autenticação
├── banco.db               # Banco de dados SQLite
├── dependencies.py        # Dependências compartilhadas
├── main.py                # Ponto de entrada da aplicação
├── models.py              # Modelos ORM (SQLAlchemy)
├── order_routes.py        # Rotas para pedidos
├── requirements.txt       # Bibliotecas utilizadas
├── schemas.py             # Schemas (Pydantic)
├── testes.py              # Arquivo de testes automatizados
├── alembic.ini            # Configuração do Alembic
├── .env                   # Variáveis de ambiente
└── .gitignore             # Arquivos ignorados pelo Git
```

---

## 🛠️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/delivery_pizzaria_api.git
cd delivery_pizzaria_api
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações do banco

```bash
alembic upgrade head
```

### 5. Inicie o servidor

```bash
uvicorn main:app --reload
```

Acesse a documentação interativa:
👉 http://127.0.0.1:8000/docs

---

## 🔐 Autenticação JWT

A API utiliza **JWT** para autenticação. Após o login, será retornado um token que deve ser utilizado como `Bearer Token` no cabeçalho de autenticação das requisições protegidas.

---

## 🧪 Testes

Você pode rodar os testes de duas formas:

### ✔️ Simplesmente executando:

```bash
python testes.py
```

### ✔️ Ou utilizando a abordagem recomendada na [documentação oficial do FastAPI](https://fastapi.tiangolo.com/advanced/testing/) com frameworks como `pytest`:

```bash
pytest
```

---

## 👨‍💻 Autor

Desenvolvido por **Jabes Christian**  
🔗 [GitHub](https://github.com/jabes-cristian) • [LinkedIn](https://www.linkedin.com/in/jabes-cristian)

