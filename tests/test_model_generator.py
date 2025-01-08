
import os
from app.models.model_generator import generate_mock_model

def test_generate_mock_model():
    model_path = "app/models/default_model.pkl"
    if os.path.exists(model_path):
        os.remove(model_path)
    generate_mock_model()
    assert os.path.exists(model_path)
