FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Use .env to load environment variables like OPENAI_API_KEY
ENV PYTHONUNBUFFERED=1

# Start the app
CMD ["python", "main.py"]
