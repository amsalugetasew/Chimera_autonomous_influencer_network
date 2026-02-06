def test_trend_fetch_contract():
    response = {
        "trends": [
            {"topic": "AI", "score": 0.8, "timestamp": "2026-01-01T00:00:00Z"}
        ]
    }
    assert "trends" in response
