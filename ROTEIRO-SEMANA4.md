# Roteiro — Semana 4 (Docker) — Atividade SOMATIVA

Objetivo desta semana: colocar a aplicação para rodar dentro de um **container
Docker**, garantir o `Dockerfile` na `main` e reunir os **4 prints** da entrega.

Arquivos já criados:

- **`Dockerfile`** — usa `python:3.12-slim`, instala as dependências, expõe a
  porta 5000, tem um `HEALTHCHECK` na rota `/health` e sobe a API com `gunicorn`.
- **`.dockerignore`** — evita copiar arquivos desnecessários para a imagem.
- Também adicionei `gunicorn` ao `requirements.txt` e um job **"Build da imagem
  Docker"** no workflow de CD, que constrói e testa o container a cada PR.

## Pré-requisito: Docker instalado

Você precisa do **Docker Desktop** aberto/rodando no seu Mac. Confira com:

```bash
docker --version
```

Se não tiver, baixe em <https://www.docker.com/products/docker-desktop/> e abra o
aplicativo antes de continuar.

## 1. Construir a imagem

No terminal, dentro da pasta do projeto:

```bash
docker build -t api-tarefas .
```

## 2. Rodar o container

```bash
docker run -d -p 5000:5000 --name api-tarefas api-tarefas
```

- `-d` roda em segundo plano;
- `-p 5000:5000` liga a porta do seu Mac à porta do container;
- `--name api-tarefas` dá um nome ao container.

## 3. Verificar que está rodando  →  PRINT 3a

```bash
docker ps
```

Você deve ver o container `api-tarefas` com status **Up** (após alguns segundos,
aparece `(healthy)`). **Tire o print desta saída do `docker ps`** — é um dos
comprovantes da entrega.

Confirme também que a API responde de dentro do container:

```bash
curl http://localhost:5000/health
curl -X POST http://localhost:5000/tarefas -H "Content-Type: application/json" -d '{"titulo":"rodando no Docker"}'
curl http://localhost:5000/tarefas
```

Para parar e remover o container depois:

```bash
docker rm -f api-tarefas
```

## 4. Colocar o Dockerfile na main (via PR)

Mantendo o padrão das semanas anteriores:

```bash
git switch main
git pull origin main
git switch -c feature/docker

git add Dockerfile .dockerignore requirements.txt .github/workflows/cd.yml ROTEIRO-SEMANA4.md
git commit -m "feat: adiciona Dockerfile e build da imagem no pipeline de CD"

git push -u origin feature/docker
```

Depois, no GitHub: **Compare & pull request → Create pull request**. Espere os
checks ficarem verdes (agora inclui o **Build da imagem Docker**) e faça
**Merge pull request → Confirm merge**. Isso garante o `Dockerfile` na `main`.

## Entrega — as 4 imagens

1. **[Semana 2]** Print do repositório com a URL e o conteúdo. ✅ (já tem)
2. **[Semana 3]** Print da PR com os workflows de CI e CD verdes. ✅ (já tem)
3. **[Semana 4 — a]** Print do `docker ps` mostrando o container rodando (passo 3).
4. **[Semana 4 — b]** Print do `Dockerfile` no repositório **ou** o próprio
   arquivo `Dockerfile` (pode anexar o arquivo direto).

## Desafio opcional (sem nota): publicar no DockerHub

Se quiser fazer o desafio, dá para o pipeline publicar a imagem automaticamente.
Duas opções — me avise qual prefere que eu configuro:

- **GitHub Container Registry (mais fácil)** — não precisa de conta nova, usa o
  próprio token do GitHub.
- **DockerHub** — como o enunciado sugere; exige criar uma conta no DockerHub e
  cadastrar dois *secrets* no repositório (`DOCKERHUB_USERNAME` e um token).
