# 📝 Todo API

API REST para gerenciamento de tarefas construída com FastAPI e SQLite.

## 🚀 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Pytest](https://pytest.org/)
- [Docker](https://www.docker.com/)

## 📋 Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | /tasks | Lista todas as tarefas |
| POST | /tasks | Cria uma nova tarefa |
| GET | /tasks/{id} | Busca uma tarefa pelo id |
| PUT | /tasks/{id} | Atualiza uma tarefa |
| DELETE | /tasks/{id} | Deleta uma tarefa |

## ⚙️ Como rodar

### Com Docker

```bash
docker compose up --build
```

### Sem Docker

```bash
# Clonar o repositório
git clone https://github.com/SEU_USUARIO/todo-api.git
cd todo-api

# Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
uvicorn main:app --reload
```

## 🧪 Como rodar os testes

```bash
pytest tests/ -v
```

## 📖 Documentação

Com a aplicação rodando, acesse:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc