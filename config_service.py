from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

ANALYSIS_URL = "https://pc-microservices.onrender.com/analyze"

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
