# API de Tarefas — DevOps (PUCPR)

Projeto desenvolvido ao longo da disciplina de **DevOps** da PUCPR. Trata-se de
uma API REST simples de lista de tarefas (to-do), construída em **Python + Flask**,
que serve de base para as atividades de CI/CD (GitHub Actions) e conteinerização
(Docker) das semanas seguintes.

## Funcionalidades

A API permite criar, listar, concluir e remover tarefas, além de retornar um
resumo com os totais.

| Método | Rota | Descrição |
| ------ | ---- | --------- |
| GET | `/` | Informações da API |
| GET | `/health` | Healthcheck |
| GET | `/tarefas` | Lista todas as tarefas |
| POST | `/tarefas` | Cria uma tarefa (JSON: `{"titulo": "..."}`) |
| GET | `/tarefas/<id>` | Obtém uma tarefa |
| POST | `/tarefas/<id>/concluir` | Marca a tarefa como concluída |
| DELETE | `/tarefas/<id>` | Remove uma tarefa |
| GET | `/resumo` | Totais (total, concluídas, pendentes) |

## Como executar localmente

```bash
# 1. Criar e ativar um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Rodar a API
python -m app.main
```

A API ficará disponível em `http://localhost:5000`.

Exemplo de uso com `curl`:

```bash
curl -X POST http://localhost:5000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "estudar DevOps"}'

curl http://localhost:5000/tarefas
```

## Testes

```bash
pip install -r requirements-dev.txt
pytest
```

## Estrutura do projeto

```
.
├── app/
│   ├── __init__.py
│   ├── main.py        # rotas Flask
│   └── services.py    # regras de negócio (testáveis)
├── tests/
│   ├── test_api.py
│   └── test_services.py
├── requirements.txt
├── requirements-dev.txt
├── setup.cfg
├── LICENSE
└── README.md
```

## Roadmap da disciplina

- [x] **Semana 2** — repositório, branch, commits e Pull Request
- [ ] **Semana 3** — CI/CD com GitHub Actions
- [ ] **Semana 4** — Docker (Dockerfile e container)
 # pequena mudanca qualquer
