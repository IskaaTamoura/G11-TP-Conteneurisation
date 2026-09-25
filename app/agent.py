import time

from app.collector import collect_metrics
from app.config import COLLECTION_INTERVAL, METRICS_ENDPOINT, REQUEST_TIMEOUT
from app.formatter import format_metrics
from app.sender import send_metrics

def run():
    while True:
        metrics = collect_metrics()
        payload = format_metrics(metrics)
        try:
            send_metrics(METRICS_ENDPOINT, payload, REQUEST_TIMEOUT)
        except Exception as exc:
            print(f"Erreur d'envoi des métriques: {exc}", flush=True)
        time.sleep(COLLECTION_INTERVAL)

if __name__ == "__main__":
    run()
