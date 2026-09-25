def test_sender_module_import():
    from app.sender import send_metrics
    assert callable(send_metrics)
