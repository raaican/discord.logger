FROM python:3.12-slim-bookworm
WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y sqlite3 \
    && pip install --break-system-packages --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN echo ".headers on\n.mode column\n.separator |" > ~/.sqliterc

COPY . .

CMD ["python3", "main.py"]
