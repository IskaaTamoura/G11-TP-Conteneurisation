import os

METRICS_ENDPOINT = os.getenv("METRICS_ENDPOINT", "http://api:8000/metrics")
COLLECTION_INTERVAL = int(os.getenv("COLLECTION_INTERVAL", "5"))
REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "5"))
