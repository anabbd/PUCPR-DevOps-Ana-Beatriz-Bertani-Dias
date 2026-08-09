# Roteiro Git — Semana 2 (repositório, branch, commits e PR)

Siga na ordem. Tudo é copiar e colar no terminal, dentro da pasta do projeto.

## 1. Criar o repositório no GitHub

1. Acesse <https://github.com/new>.
2. **Repository name**: algo que tenha ligação com seu nome — sugestão:
   `devops-api-tarefas` (o professor exige que o usuário/repositório seja
   identificável como seu; sua conta já é `bertani.anabeatriz`, então está ok).
3. Marque **Public**.
4. **NÃO** marque "Add a README", ".gitignore" nem "License" — deixe **vazio**
   (a atividade pede repositório preferencialmente vazio e nós já temos esses
   arquivos localmente).
5. Clique em **Create repository** e copie a URL que aparece, algo como
   `https://github.com/SEU-USUARIO/devops-api-tarefas.git`.

## 2. Inicializar o Git e fazer o commit inicial na main

Abra o terminal na pasta do projeto (a pasta `DevOPS` onde estão os arquivos):

```bash
git init -b main
git add .gitignore LICENSE
git commit -m "chore: commit inicial com licenca e gitignore"
```

## 3. Criar o branch de trabalho e os commits

```bash
git switch -c feature/api-tarefas

git add requirements.txt requirements-dev.txt setup.cfg
git commit -m "chore: adiciona dependencias e configuracao (flake8/pytest)"

git add app/__init__.py app/services.py
git commit -m "feat: regras de negocio da API de tarefas"

git add app/main.py
git commit -m "feat: rotas Flask da API (CRUD de tarefas)"

git add tests/__init__.py tests/test_services.py
git commit -m "test: testes das regras de negocio"

git add tests/test_api.py
git commit -m "test: testes das rotas HTTP"

git add README.md ROTEIRO-GIT.md
git commit -m "docs: README com instrucoes de uso e roadmap"
```

Isso gera **6 commits** no branch `feature/api-tarefas`, além do commit inicial
na `main` (atende a exigência de "5 ou mais commits").

## 4. Enviar tudo para o GitHub

Troque a URL abaixo pela que você copiou no passo 1:

```bash
git remote add origin https://github.com/SEU-USUARIO/devops-api-tarefas.git

# envia a main (commit inicial)
git switch main
git push -u origin main

# envia o branch de trabalho
git switch feature/api-tarefas
git push -u origin feature/api-tarefas
```

## 5. Abrir e mergear a Pull Request

1. No GitHub, o repositório mostrará um aviso **"Compare & pull request"** —
   clique nele. (Se não aparecer, vá na aba **Pull requests → New pull request**,
   base = `main`, compare = `feature/api-tarefas`.)
2. Dê um título, ex.: `Implementa API de Tarefas`, e clique em
   **Create pull request**.
3. Como você mesma pode aprovar, clique em **Merge pull request → Confirm merge**.

## 6. Print para entrega

Tire um screenshot mostrando:

- A **URL do repositório** visível na barra de endereços (fundo escuro do
  navegador), com seu usuário e o nome do repositório;
- O **conteúdo** do repositório (a listagem de arquivos na página inicial).

Pronto! Esse print é a entrega da atividade formativa da semana 2.

---

### Dica: atualizar seu nome nos commits (opcional)

Se quiser que os commits saiam com seu nome e e-mail, rode antes do passo 2:

```bash
git config --global user.name "Ana Beatriz Bertani"
git config --global user.email "bertani.anabeatriz@gmail.com"
```
