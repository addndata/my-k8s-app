FROM python:3.8-slim

WORKDIR /app

COPY client.py /app/client.py

CMD ["python", "/app/client.py"]
