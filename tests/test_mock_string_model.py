
import pytest
from app.models.mock_string_model import MockStringModel

def test_mock_model_fit():
    model = MockStringModel()
    assert model.fit(["input"]) == model

def test_mock_model_predict():
    model = MockStringModel()
    result = model.predict(["test input"])
    assert result == ["Processed: test input"]
