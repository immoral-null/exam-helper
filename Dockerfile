FROM python:3.11-slim

RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Run app as appuser
CMD ["/app/command.sh"]