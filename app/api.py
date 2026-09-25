from fastapi import FastAPI

app = FastAPI(title="System Metrics Agent API")

_latest_metrics = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/metrics")
def receive_metrics(payload: dict):
    global _latest_metrics
    _latest_metrics = payload
    return {"status": "received"}

@app.get("/metrics")
def metrics():
    return _latest_metrics

@app.get("/metrics/latest")
def latest_metrics():
    return _latest_metrics
