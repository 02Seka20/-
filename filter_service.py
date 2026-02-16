from fastapi import FastAPI

app = FastAPI()

components_db = [
    {"name": "Intel i5", "type": "CPU", "price": 200},
    {"name": "Ryzen 5", "type": "CPU", "price": 220},
    {"name": "GTX 1660", "type": "GPU", "price": 300}
]

@app.get("/filter/{component_type}")
def filter_by_type(component_type: str):
    return [c for c in components_db if c["type"] == component_type]
