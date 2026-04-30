FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    curl \
    chromium \
    chromium-driver \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .


RUN pip install --no-cache-dir -r requirements.txt

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

EXPOSE 8000

# Comando padrão: 
# 1. Sobe o servidor da aplicação
# 2. Executa os testes automatizados
CMD python -m http.server 8000 & pytest -v
