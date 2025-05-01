# 🚀 Twitter Sentiment Analysis using BERT with CI/CD Pipeline

This project implements a **Sentiment Analysis API** powered by a **BERT-based model**, served via **FastAPI** and automated using **GitHub Actions CI/CD**.  
It classifies tweets as **positive**, **negative**, or **neutral** or **Irrelevant**.in real-time.

---

## 📌 Project Highlights

- ✅ **Transformer Model**: Fine-tuned BERT for sentiment classification  
- ⚙️ **FastAPI**: Lightweight and fast RESTful API  
- 🐳 **Dockerized**: Fully containerized for easy deployment  
- 🚀 **CI/CD with GitHub Actions**:  
  - On every push to `main` branch:
    - Builds and tags Docker image
    - Pushes the image to [Docker Hub](https://hub.docker.com/)
    

---

## 🧠 Model Training

The sentiment analysis model was trained using BERT and is available in this separate repository:  
🔗 [Model Training Code on GitHub](https://github.com/bijenkoiri/twitter-sentiment-analysis-bert.git)

---

## 🛠️ Tech Stack

| Component      | Tool |
|----------------|------|
| Language       | Python 3.10 |
| Model          | BERT (Transformers) |
| API Framework  | FastAPI |
| Containerization | Docker |
| CI/CD          | GitHub Actions |


---

## 🔁 CI/CD Pipeline

This project includes a GitHub Actions workflow that automates the following:

1. **On Push to `main`**:
   - ✅ Runs a test server to verify the API launches
   - 🐳 Builds the Docker image with tag `:commit-sha`
   - ☁️ Pushes the image to Docker Hub
   

You can find the pipeline config in `.github/workflows/ci-cd.yml`.

---

## 📦 How to Run Locally

```bash
# Clone this repository
git clone https://github.com/bijenkoiri/sentimentmlapi.git
cd sentimentmlapi

# Download model folder
gdown --folder https://drive.google.com/drive/folders/1_g6NKcUfkpUOKgbq1vBio1Pm5DmIeHAA

# Run the API
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
