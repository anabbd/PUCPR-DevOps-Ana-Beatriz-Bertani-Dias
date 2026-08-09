"""API de Tarefas (to-do) construida com Flask.

Rotas:
    GET    /              -> informacoes da API
    GET    /health        -> healthcheck (usado pelo Docker/CI)
    GET    /tarefas       -> lista as tarefas
    POST   /tarefas       -> cria uma tarefa   (JSON: {"titulo": "..."})
    GET    /tarefas/<id>  -> obtem uma tarefa
    POST   /tarefas/<id>/concluir -> marca como concluida
    DELETE /tarefas/<id>  -> remove uma tarefa
    GET    /resumo        -> totais de tarefas
"""

from __future__ import annotations

from flask import Flask, jsonify, request

from app.services import ErroDeValidacao, RepositorioTarefas, resumo


def criar_app(repositorio: RepositorioTarefas | None = None) -> Flask:
    app = Flask(__name__)
    repo = repositorio or RepositorioTarefas()

    @app.get("/")
    def raiz():
        return jsonify(
            {
                "aplicacao": "API de Tarefas",
                "versao": "1.0.0",
                "descricao": "Projeto da disciplina de DevOps (PUCPR).",
            }
        )

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/tarefas")
    def listar_tarefas():
        return jsonify(repo.listar())

    @app.post("/tarefas")
    def criar_tarefa():
        dados = request.get_json(silent=True) or {}
        try:
            tarefa = repo.criar(dados.get("titulo"))
        except ErroDeValidacao as erro:
            return jsonify({"erro": str(erro)}), 400
        return jsonify(tarefa), 201

    @app.get("/tarefas/<int:tarefa_id>")
    def obter_tarefa(tarefa_id: int):
        tarefa = repo.obter(tarefa_id)
        if tarefa is None:
            return jsonify({"erro": "Tarefa nao encontrada."}), 404
        return jsonify(tarefa)

    @app.post("/tarefas/<int:tarefa_id>/concluir")
    def concluir_tarefa(tarefa_id: int):
        tarefa = repo.concluir(tarefa_id)
        if tarefa is None:
            return jsonify({"erro": "Tarefa nao encontrada."}), 404
        return jsonify(tarefa)

    @app.delete("/tarefas/<int:tarefa_id>")
    def remover_tarefa(tarefa_id: int):
        if not repo.remover(tarefa_id):
            return jsonify({"erro": "Tarefa nao encontrada."}), 404
        return "", 204

    @app.get("/resumo")
    def obter_resumo():
        return jsonify(resumo(repo.listar()))

    return app


app = criar_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
