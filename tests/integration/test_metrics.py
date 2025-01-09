from fastapi.testclient import TestClient
from app.main import app
from app.utils.metrics import PREDICTION_HIT_COUNTER, PREDICTION_RESPONSE_TIME

client = TestClient(app)

def test_metrics_increment():
    initial_count = PREDICTION_HIT_COUNTER._value.get()
    client.post("/predict/test_model", json={"input": "test"})
    assert PREDICTION_HIT_COUNTER._value.get() == initial_count + 1
