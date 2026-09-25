import requests

def send_metrics(endpoint: str, payload: dict, timeout: float = 5):
    response = requests.post(endpoint, json=payload, timeout=timeout)
    response.raise_for_status()
    return response
