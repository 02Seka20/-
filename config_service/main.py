from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests
from fastapi.responses import HTMLResponse
app = FastAPI()

ANALYSIS_URL = "http://127.0.0.1:8003/analyze"

class ConfigurationRequest(BaseModel):
    component_ids: List[int]

components_db = {
    1: {"name": "CPU", "type": "processor", "price": 300.0, "power": 95},
    2: {"name": "GPU", "type": "graphics", "price": 500.0, "power": 250},
    3: {"name": "RAM", "type": "memory", "price": 150.0, "power": 40},
}

@app.post("/configurations")
def create_configuration(config: ConfigurationRequest):

    selected = [
        components_db[i]
        for i in config.component_ids
        if i in components_db
    ]

    response = requests.post(
        ANALYSIS_URL,
        json={"components": selected}
    )

    return response.json()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
    <body>
        <h2>PC Configurator</h2>
        <button onclick="send()">Analyze</button>
        <pre id="result"></pre>

        <script>
        async function send() {
            const response = await fetch("/configurations", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({component_ids:[1,2]})
            });
            const data = await response.json();
            document.getElementById("result").innerText =
                JSON.stringify(data, null, 2);
        }
        </script>
    </body>
    </html>
    """