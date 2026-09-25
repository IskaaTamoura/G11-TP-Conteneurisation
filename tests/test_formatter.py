from app.formatter import format_metrics

def test_format_metrics():
    result = format_metrics({"cpu_percent": 10})
    assert result["cpu_percent"] == 10
    assert "timestamp" in result
