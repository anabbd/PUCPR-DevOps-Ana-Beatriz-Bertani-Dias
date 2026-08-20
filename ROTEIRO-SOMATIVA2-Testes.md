# Roteiro — Atividade Somativa 2 (Testes unitários em PR)

Objetivo: ter pelo menos **5 testes unitários** rodando **a cada commit numa PR**
(via GitHub Actions) e reunir os prints da entrega.

## O que já estava pronto (desde a semana 3)

- O projeto já tem testes unitários em `tests/test_services.py` e `tests/test_api.py`.
- O workflow **`ci.yml`** já roda `pytest` no gatilho `pull_request`, ou seja,
  **os testes rodam a cada novo commit em uma PR** para a `main`.

## O que adicionei agora

- **`tests/test_services_extra.py`** — 7 testes unitários novos (casos de borda:
  IDs sequenciais, itens inexistentes, limite de tamanho do título, resumo vazio).
- Total do projeto: **20 testes**, todos passando (`flake8` limpo).

---

## Passo a passo

1. Atualize a `main` e crie o branch desta atividade:

   ```bash
   git switch main
   git pull origin main
   git switch -c feature/testes-unitarios
   ```

2. Adicione os testes novos e o roteiro, e faça o commit:

   ```bash
   git add tests/test_services_extra.py ROTEIRO-SOMATIVA2-Testes.md
   git commit -m "test: adiciona testes unitarios extras (somativa 2)"
   git push -u origin feature/testes-unitarios
   ```

3. No GitHub, abra a **PR** (`feature/testes-unitarios` → `main`).

4. Assim que a PR abre, o GitHub Actions roda os workflows. Espere ficar verde:
   você verá os checks **CI / Testes (pytest) (3.10 / 3.11 / 3.12)** rodando os
   testes dentro da PR.

5. (Opcional, para mostrar que roda "a cada commit") faça mais um commit na mesma
   branch e observe os testes rodando de novo:

   ```bash
   git commit --allow-empty -m "test: novo commit para disparar os testes na PR"
   git push
   ```

---

## Prints da entrega (Somativa 2)

Como você **já entregou a Somativa 1**, não precisa repetir os prints das semanas
2, 3 e 4. Para a Somativa 2, junte:

**[Da semana 6 — alertas]**
1. Print do arquivo de workflow com a config dos alertas (`notify-discord.yml`).
2. Print de alguns alertas recebidos no Discord.
   > Você já tem os dois: `#6 - Semana6 - 1 Workflow alertas.png` e
   > `#6 - Semana6 - 2 Alertas recebidos.png`.

**[Desta semana — testes]**
3. Print(s) do **código dos testes unitários** (abra no GitHub, ex.:
   `.../blob/main/tests/test_services_extra.py` e/ou `test_services.py`,
   `test_api.py`). Alternativa: enviar os próprios arquivos de teste.
4. Pelo menos um print mostrando os **testes executados dentro de uma PR** — a
   página da PR com os checks de `pytest` verdes.

---

### Lista dos testes unitários (resumo)

- `tests/test_services.py` — 7 testes (validação de título, criar/listar,
  concluir, remover, resumo).
- `tests/test_services_extra.py` — 7 testes (IDs sequenciais, itens inexistentes,
  limite de título, resumo vazio).
- `tests/test_api.py` — 6 testes das rotas HTTP (health, criar, 400, 404,
  concluir, resumo).
