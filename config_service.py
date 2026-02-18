from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

ANALYSIS_URL = "https://pc-microservices.onrender.com/analyze"

class ConfigurationRequest(BaseModel):
    component_ids: List[int]

@app.post("/configurations")
def create_configuration(config: ConfigurationRequest):
    # Мок ответа от analysis_service
    selected_components = [
        {"id": i, "name": f"Component {i}", "price": i*100, "power": i*50}
        for i in config.component_ids
    ]
    total_price = sum(c["price"] for c in selected_components)
    total_power = sum(c["power"] for c in selected_components)
    return {
        "selected_components": selected_components,
        "total_price": total_price,
        "total_power": total_power
    }
