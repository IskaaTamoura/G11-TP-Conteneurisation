from datetime import datetime, timezone

def format_metrics(metrics: dict) -> dict:
    return {
        **metrics,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
