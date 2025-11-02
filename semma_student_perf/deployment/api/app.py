from fastapi import FastAPI
from pydantic import BaseModel
import joblib, pandas as pd, os

MODEL_PATH = os.getenv("MODEL_PATH", "deployment/model.joblib")
app = FastAPI(title="Model Inference API", version="0.1.0")

class Item(BaseModel):
    # Accept flexible JSON payload of features
    features: dict

@app.on_event("startup")
def load_model():
    global model
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        model = None
        print("Model not loaded:", e)

@app.get("/health")
def health():
    return {"ok": model is not None}

@app.post("/predict")
def predict(item: Item):
    if model is None:
        return {"error": "Model not loaded"}
    X = pd.DataFrame([item.features])
    yhat = model.predict_proba(X)[:, 1] if hasattr(model, "predict_proba") else model.predict(X)
    return {"prediction": float(yhat[0]) if not isinstance(yhat, float) else yhat}
