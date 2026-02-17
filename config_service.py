from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

ANALYSIS_URL = "https://pc-microservices.onrender.com/analyze"

# -----------------------------
# Модель входных данных
# -----------------------------
class ConfigurationRequest(BaseModel):
    component_ids: List[int]

# -----------------------------
# Создать конфигурацию
# -----------------------------
@app.post("/configurations")
def create_configuration(config: ConfigurationRequest):
    try:
        # Отправляем POST в analysis_service
        response = requests.post(
            ANALYSIS_URL,
            json={"component_ids": config.component_ids}
        )
        return response.json()
    except Exception as e:
        return {"error": f"Analysis service unavailable: {str(e)}"}

# -----------------------------
# Проверка работы
# -----------------------------
@app.get("/")
def root():
    return {"message": "Configuration Service is running"}
