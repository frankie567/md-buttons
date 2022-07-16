FROM python:3.10-slim

WORKDIR /app
ENV PORT=8000

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install -y fonts-liberation && \
    pip install -U pip && \
    pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "uvicorn md_buttons.app:app --host 0.0.0.0 --port $PORT"]
