from app.collector import collect_metrics

def test_collect_metrics():
    result = collect_metrics()
    assert "cpu_percent" in result
    assert "memory_percent" in result
