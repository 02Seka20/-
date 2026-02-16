from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# -----------------------------
# Модель комплектующего
# -----------------------------
class Component(BaseModel):
    id: int
    name: str
    type: str
    power: float
    price: float


# -----------------------------
# Хранилище (пока в памяти)
# -----------------------------
components: List[Component] = []


# -----------------------------
# Получить все комплектующие
# -----------------------------
@app.get("/components")
def get_components():
    return components


# -----------------------------
# Получить комплектующее по ID
# -----------------------------
@app.get("/components/{component_id}")
def get_component(component_id: int):
    for comp in components:
        if comp.id == component_id:
            return comp
    return {"error": "Component not found"}


# -----------------------------
# Добавить комплектующее
# -----------------------------
@app.post("/components")
def add_component(component: Component):
    components.append(component)
    return {"message": "Component added", "component": component}


# -----------------------------
# Удалить комплектующее
# -----------------------------
@app.delete("/components/{component_id}")
def delete_component(component_id: int):
    global components
    components = [c for c in components if c.id != component_id]
    return {"message": "Component deleted"}
