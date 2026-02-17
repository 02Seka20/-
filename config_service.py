from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

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
        response = requests.post(
            ANALYSIS_URL,
            json={"component_ids": config.component_ids}
        )
        return response.json()
    except Exception:
        return {"error": "Analysis service unavailable"}

# -----------------------------
# Проверка работы
# -----------------------------
@app.get("/")
def root():
    return {"message": "Configuration Service is running"}
