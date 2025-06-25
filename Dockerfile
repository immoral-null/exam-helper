FROM python:3.11-slim

RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

CMD ["python", "main.py"]
