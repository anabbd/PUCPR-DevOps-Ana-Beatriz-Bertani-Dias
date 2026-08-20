"""Testes unitarios adicionais das regras de negocio (Atividade Somativa 2).

Cobrem casos de borda que reforcam a cobertura das funcoes em app/services.py.
"""

import pytest

from app.services import (
    ErroDeValidacao,
    RepositorioTarefas,
    resumo,
    validar_titulo,
)


def test_criar_incrementa_ids_sequencialmente():
    repo = RepositorioTarefas()
    primeira = repo.criar("primeira")
    segunda = repo.criar("segunda")
    assert primeira["id"] == 1
    assert segunda["id"] == 2


def test_obter_tarefa_inexistente_retorna_none():
    repo = RepositorioTarefas()
    assert repo.obter(999) is None


def test_concluir_tarefa_inexistente_retorna_none():
    repo = RepositorioTarefas()
    assert repo.concluir(42) is None


def test_remover_tarefa_inexistente_retorna_false():
    repo = RepositorioTarefas()
    assert repo.remover(7) is False


def test_validar_titulo_muito_longo_falha():
    titulo_grande = "a" * 121
    with pytest.raises(ErroDeValidacao):
        validar_titulo(titulo_grande)


def test_validar_titulo_no_limite_maximo_ok():
    titulo_no_limite = "a" * 120
    assert validar_titulo(titulo_no_limite) == titulo_no_limite


def test_resumo_de_lista_vazia():
    assert resumo([]) == {"total": 0, "concluidas": 0, "pendentes": 0}
