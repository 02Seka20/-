from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd

app = FastAPI()

class Component(BaseModel):
    name: str
    type: str
    price: float
    power: int

class Configuration(BaseModel):
    components: List[Component]

@app.post("/analyze")
def analyze_config(config: Configuration):
    df = pd.DataFrame([c.dict() for c in config.components])
    
    total_price = df["price"].sum()
    total_power = df["power"].sum()
    avg_price = df["price"].mean()

    return {
        "total_price": float(total_price),
        "total_power": int(total_power),
        "average_price": float(avg_price)
    }
