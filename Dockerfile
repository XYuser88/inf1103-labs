FROM python:3.11-slim
WORKDIR /app
COPY OOPStoreManager.py .
CMD ["python", "OOPStoreManager.py"]