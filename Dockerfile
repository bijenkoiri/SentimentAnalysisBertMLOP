FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install gdown for downloading from Google Drive
RUN pip install gdown

COPY . .

# Make startup script executable
RUN chmod +x startup.sh

EXPOSE 8000

CMD ["./startup.sh"]
