"""Regras de negocio da API de Tarefas.

Estas funcoes nao dependem do Flask, o que as torna faceis de testar
de forma isolada (bom para o pipeline de CI da semana 3).
"""

from __future__ import annotations

from typing import Dict, List, Optional


class ErroDeValidacao(Exception):
    """Levantada quando os dados de uma tarefa sao invalidos."""


class RepositorioTarefas:
    """Armazena tarefas em memoria.

    Simples de proposito: o foco da disciplina e o fluxo de DevOps
    (CI/CD, Docker), e nao a persistencia em banco de dados.
    """

    def __init__(self) -> None:
        self._tarefas: Dict[int, dict] = {}
        self._proximo_id: int = 1

    def listar(self) -> List[dict]:
        return list(self._tarefas.values())

    def obter(self, tarefa_id: int) -> Optional[dict]:
        return self._tarefas.get(tarefa_id)

    def criar(self, titulo: str) -> dict:
        titulo = validar_titulo(titulo)
        tarefa = {"id": self._proximo_id, "titulo": titulo, "concluida": False}
        self._tarefas[self._proximo_id] = tarefa
        self._proximo_id += 1
        return tarefa

    def concluir(self, tarefa_id: int) -> Optional[dict]:
        tarefa = self._tarefas.get(tarefa_id)
        if tarefa is None:
            return None
        tarefa["concluida"] = True
        return tarefa

    def remover(self, tarefa_id: int) -> bool:
        return self._tarefas.pop(tarefa_id, None) is not None


def validar_titulo(titulo: object) -> str:
    """Valida e normaliza o titulo de uma tarefa."""
    if not isinstance(titulo, str):
        raise ErroDeValidacao("O titulo deve ser um texto.")
    titulo_limpo = titulo.strip()
    if not titulo_limpo:
        raise ErroDeValidacao("O titulo nao pode ser vazio.")
    if len(titulo_limpo) > 120:
        raise ErroDeValidacao("O titulo deve ter no maximo 120 caracteres.")
    return titulo_limpo


def resumo(tarefas: List[dict]) -> dict:
    """Retorna um resumo com totais de tarefas."""
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t.get("concluida"))
    return {
        "total": total,
        "concluidas": concluidas,
        "pendentes": total - concluidas,
    }
