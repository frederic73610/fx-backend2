
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser les appels du frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict")
def predict(symbol: str = "EUR/USD", interval: str = "1day"):
    return {"prediction": "Il y a 65.1% de chances que le taux de change augmente ⬆️."}
