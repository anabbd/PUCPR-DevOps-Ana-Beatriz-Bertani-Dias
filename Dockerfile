# Imagem base enxuta com Python 3.12
FROM python:3.12-slim

# Boas praticas: nao gerar .pyc e enviar logs direto para o terminal
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Instala as dependencias primeiro (aproveita o cache de camadas do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o codigo da aplicacao
COPY app ./app

# Porta em que a API sera exposta
EXPOSE 5000

# Verifica periodicamente se a aplicacao esta saudavel (rota /health)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:5000/health').status==200 else 1)"

# Sobe a API com o servidor gunicorn (pronto para producao)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]
