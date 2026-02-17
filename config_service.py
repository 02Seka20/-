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
    try:
        response = requests.post(
            ANALYSIS_URL,
            json={"components": config.component_ids}  # <--- важно
        )
        return response.json()
    except Exception as e:
        return {"error": f"Analysis service unavailable: {str(e)}"}

@app.get("/")
def root():
    return {"message": "Configuration Service is running"}
