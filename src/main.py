from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")

# Định dạng dữ liệu đầu vào
class SentimentRequest(BaseModel):
    text: str

# Định dạng dữ liệu đầu ra
class SentimentResponse(BaseModel):
    text: str
    label: str
    score: float

@app.get("/health")
def health_check():
    """Tiêu chí (b): Endpoint để Kubernetes kiểm tra sức khỏe ứng dụng"""
    return {"status": "healthy"}

@app.post("/predict", response_model=SentimentResponse)
async def predict(request: SentimentRequest):
    """
    Logic chính: Tiếp nhận text và gửi đến model hoặc xử lý trực tiếp.
    Mai có thể thêm logic gọi tới KServe InferenceService tại đây.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    # Giả lập logic dự báo (Mai sẽ thay bằng logic gọi Model thật sau)
    # Ví dụ: Một logic đơn giản để pass Pytest trước
    dummy_label = "POSITIVE" if "love" in request.text.lower() else "NEGATIVE"
    
    return {
        "text": request.text,
        "label": dummy_label,
        "score": 0.95
    }

if __name__ == "__main__":
    # Chạy trên port 8080 để khớp với cấu hình Docker thường dùng trong K8s
    uvicorn.run(app, host="0.0.0.0", port=8080)