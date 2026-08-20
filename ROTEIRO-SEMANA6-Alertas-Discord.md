# Roteiro — Semana 6 (Alertas no Discord) — Atividade FORMATIVA

Objetivo: configurar o GitHub Actions para enviar um **alerta no Discord** a cada
push/merge na `main`, e entregar **2 prints**:
1. o arquivo de workflow com a configuração do alerta;
2. os alertas recebidos no Discord.

Já criei o workflow **`.github/workflows/notify-discord.yml`**. Ele usa um
*webhook* do Discord guardado num secret (`DISCORD_WEBHOOK`), sem expor nada.

---

## Parte A — Criar o webhook no Discord

1. Abra o **Discord**. Se não tiver um servidor, crie um: clique no **+** na
   barra lateral esquerda → **Criar meu próprio** → dê um nome (ex.: "DevOps PUCPR").
2. Escolha (ou crie) um canal de texto, ex.: **#alertas**.
3. Passe o mouse no canal → ⚙️ **Editar canal** → **Integrações** → **Webhooks**
   → **Novo webhook**.
4. Dê um nome ao webhook (ex.: "GitHub Actions") e clique em **Copiar URL do
   webhook**. Guarde essa URL (é como uma senha — não compartilhe).

## Parte B — Cadastrar o secret no GitHub

1. Abra:
   `github.com/anabbd/PUCPR-DevOps-Ana-Beatriz-Bertani-Dias/settings/secrets/actions`
2. **New repository secret**:
   - **Name:** `DISCORD_WEBHOOK`
   - **Secret:** cole a URL do webhook copiada no passo A.4
3. **Add secret**.

## Parte C — Enviar o workflow para o repositório

No terminal, na pasta do projeto:

```bash
git switch main
git pull origin main
git switch -c feature/alertas-discord
git add .github/workflows/notify-discord.yml ROTEIRO-SEMANA6-Alertas-Discord.md
git commit -m "ci: adiciona alertas no Discord a cada push na main"
git push -u origin feature/alertas-discord
```

Depois, no GitHub: abra a **PR** (`feature/alertas-discord` → `main`) e faça o
**Merge**. O merge é um push na `main` → dispara o primeiro alerta no Discord. 🎉

## Parte D — Gerar "alguns" alertas

Para o print ter mais de um alerta, faça mais uma ou duas alterações que cheguem
na `main`. O jeito mais simples:

```bash
git switch main
git pull origin main
echo "" >> README.md            # pequena mudanca qualquer
git commit -am "docs: pequena atualizacao para testar alerta"
git push origin main
```

Cada push na `main` gera um novo alerta no canal do Discord.

## Parte E — Os 2 prints da entrega

1. **Workflow:** abra o arquivo no GitHub e tire o print (com a URL visível):
   `github.com/anabbd/PUCPR-DevOps-Ana-Beatriz-Bertani-Dias/blob/main/.github/workflows/notify-discord.yml`
2. **Alertas recebidos:** tire o print do **canal do Discord** mostrando as
   mensagens de alerta que chegaram (com o título "🚀 Novo push na main" etc.).

---

### Observações

- O alerta dispara em **push na `main`** (inclui merges de PR). Se preferir alerta
  em *todo* commit de qualquer branch, me avise que troco o gatilho para
  `on: push` sem filtro de branch.
- Se o alerta não chegar, confira na aba **Actions** se o workflow "Alertas no
  Discord" rodou e veja o log do passo — normalmente é o secret `DISCORD_WEBHOOK`
  ausente ou com URL incompleta.
