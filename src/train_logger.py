import mlflow
import mlflow.transformers
from transformers import pipeline

def log_model_to_mlflow():
    # 1. Chọn model nhỏ gọn từ HuggingFace
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)

    # 2. Bắt đầu log vào MLFlow
    mlflow.set_experiment("AIDE_Final_Project")
    
    with mlflow.start_run():
        # Log các tham số cơ bản
        mlflow.log_param("model_name", model_name)
        mlflow.log_param("task", "sentiment-analysis")
        
        # Log model chính (Sau này KServe sẽ kéo model từ đây)
        mlflow.transformers.log_model(
            transformers_model=sentiment_pipeline,
            artifact_path="sentiment_model"
        )
        print("Đã log model lên MLFlow thành công!")

if __name__ == "__main__":
    log_model_to_mlflow()