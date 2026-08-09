"""Testes das rotas HTTP da API."""

import pytest

from app.main import criar_app
from app.services import RepositorioTarefas


@pytest.fixture
def cliente():
    app = criar_app(RepositorioTarefas())
    app.testing = True
    return app.test_client()


def test_health(cliente):
    resposta = cliente.get("/health")
    assert resposta.status_code == 200
    assert resposta.get_json() == {"status": "ok"}


def test_criar_tarefa(cliente):
    resposta = cliente.post("/tarefas", json={"titulo": "estudar DevOps"})
    assert resposta.status_code == 201
    corpo = resposta.get_json()
    assert corpo["titulo"] == "estudar DevOps"
    assert corpo["concluida"] is False


def test_criar_tarefa_sem_titulo_retorna_400(cliente):
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == 400


def test_obter_tarefa_inexistente_retorna_404(cliente):
    resposta = cliente.get("/tarefas/999")
    assert resposta.status_code == 404


def test_fluxo_concluir_tarefa(cliente):
    cliente.post("/tarefas", json={"titulo": "escrever testes"})
    resposta = cliente.post("/tarefas/1/concluir")
    assert resposta.status_code == 200
    assert resposta.get_json()["concluida"] is True


def test_resumo(cliente):
    cliente.post("/tarefas", json={"titulo": "a"})
    cliente.post("/tarefas", json={"titulo": "b"})
    cliente.post("/tarefas/1/concluir")
    resposta = cliente.get("/resumo")
    assert resposta.get_json() == {"total": 2, "concluidas": 1, "pendentes": 1}
