# Example: portfolio/services/main-api/Dockerfile
FROM python:3.11-slim

# # Install system dependencies (if needed for OCR, PDF, etc.)
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     tesseract-ocr \
#     poppler-utils \
#     libgl1 \
#     && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
