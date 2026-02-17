from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

COMPONENTS_URL = "https://pc-microservices.onrender.com/components"

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
    response = requests.get(COMPONENTS_URL)
    components = response.json()

    selected = []
    total_price = 0
    total_power = 0

    for comp in components:
        if comp["id"] in config.component_ids:
            selected.append(comp)
            total_price += comp["price"]
            total_power += comp["power"]

    return {
        "selected_components": selected,
        "total_price": total_price,
        "total_power": total_power
    }


# -----------------------------
# Проверка работы
# -----------------------------
@app.get("/")
def root():
    return {"message": "Configuration Service is running"}
