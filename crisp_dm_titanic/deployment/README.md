To serve locally after training:
```
MODEL_PATH=deployment/model.joblib uvicorn deployment.api.app:app --reload --port 8000
```
