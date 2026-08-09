# Roteiro — Semana 3 (CI/CD com GitHub Actions)

Objetivo: abrir uma PR em que **todos os workflows (CI e CD) passam com sucesso**
e tirar o print para a entrega.

Já criei dois workflows na pasta `.github/workflows/`:

- **`ci.yml` (CI)** — roda `flake8` (lint) e `pytest` nas versões 3.10, 3.11 e 3.12.
- **`cd.yml` (CD)** — roda os testes como gate de qualidade e empacota a aplicação
  num artefato de deploy (`api-tarefas.tar.gz`), publicado no próprio Actions.

Ambos disparam em `push` na `main` e em toda `pull_request` para a `main`.

## 1. Atualizar a main local

Como você mergeou a PR da semana 2 pelo site, sua `main` local está atrasada.
No terminal, dentro da pasta do projeto:

```bash
git switch main
git pull origin main
```

## 2. Criar o branch da semana 3 e commitar os workflows

```bash
git switch -c feature/ci-cd

git add .github/workflows/ci.yml .github/workflows/cd.yml ROTEIRO-SEMANA3.md
git commit -m "ci: adiciona workflows de CI (lint+testes) e CD (build+artefato)"

git push -u origin feature/ci-cd
```

## 3. Abrir a Pull Request

1. No GitHub, clique em **Compare & pull request** (ou aba **Pull requests →
   New pull request**, base = `main`, compare = `feature/ci-cd`).
2. Título sugerido: `Configura CI/CD com GitHub Actions`.
3. Clique em **Create pull request**.

Assim que a PR é criada, o GitHub começa a rodar os workflows automaticamente.

## 4. Esperar os checks ficarem verdes

Na página da PR, role até o bloco de **checks**. Em 1–2 minutos você verá algo como:

- ✅ **CI / Lint (flake8)**
- ✅ **CI / Testes (pytest) (3.10)**
- ✅ **CI / Testes (pytest) (3.11)**
- ✅ **CI / Testes (pytest) (3.12)**
- ✅ **CD / Build e empacotamento**

Com a mensagem **"All checks have passed"**.

> Dica: você também pode acompanhar a execução na aba **Actions** do repositório.

## 5. Print para entrega

Tire um screenshot mostrando:

- A **URL** do repositório/PR visível na barra de endereço (fundo escuro);
- Os **checks verdes** de CI e CD (o bloco "All checks have passed" na PR, ou
  a execução verde na aba **Actions**).

Depois de tirar o print, você **pode mergear** a PR (opcional para esta entrega,
mas recomendado para deixar os workflows também na `main`):

```
Merge pull request → Confirm merge
```

## Observação sobre CD

Nesta semana o CD entrega um **artefato empacotado** (padrão de *continuous
delivery*): o resultado do build fica pronto para ser implantado. Na **semana 4**
vamos evoluir esse mesmo pipeline para construir a imagem **Docker** da aplicação.
