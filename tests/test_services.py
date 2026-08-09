"""Testes das regras de negocio (sem Flask)."""

import pytest

from app.services import (
    ErroDeValidacao,
    RepositorioTarefas,
    resumo,
    validar_titulo,
)


def test_validar_titulo_remove_espacos():
    assert validar_titulo("  estudar DevOps  ") == "estudar DevOps"


def test_validar_titulo_vazio_falha():
    with pytest.raises(ErroDeValidacao):
        validar_titulo("   ")


def test_validar_titulo_nao_texto_falha():
    with pytest.raises(ErroDeValidacao):
        validar_titulo(123)


def test_criar_e_listar_tarefa():
    repo = RepositorioTarefas()
    tarefa = repo.criar("estudar CI/CD")
    assert tarefa["id"] == 1
    assert tarefa["concluida"] is False
    assert repo.listar() == [tarefa]


def test_concluir_tarefa():
    repo = RepositorioTarefas()
    repo.criar("estudar Docker")
    tarefa = repo.concluir(1)
    assert tarefa["concluida"] is True


def test_remover_tarefa():
    repo = RepositorioTarefas()
    repo.criar("tarefa temporaria")
    assert repo.remover(1) is True
    assert repo.remover(1) is False


def test_resumo():
    repo = RepositorioTarefas()
    repo.criar("a")
    repo.criar("b")
    repo.concluir(1)
    assert resumo(repo.listar()) == {
        "total": 2,
        "concluidas": 1,
        "pendentes": 1,
    }
