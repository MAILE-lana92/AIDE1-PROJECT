# Sử dụng bản slim để giảm dung lượng image
FROM python:3.9-slim

WORKDIR /app

# Copy file requirements trước để tận dụng Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Port 8080 là port mặc định của nhiều dịch vụ Google Cloud
EXPOSE 8080

CMD ["python", "src/main.py"]