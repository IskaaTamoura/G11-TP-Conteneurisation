import os
import psutil

def collect_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "load_1m": os.getloadavg()[0] if hasattr(os, "getloadavg") else None,
    }
