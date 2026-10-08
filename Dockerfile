FROM python:3.11-slim
WORKDIR /app
COPY ModularAuditor.py .
CMD ["python", "ModularAuditor.py"]