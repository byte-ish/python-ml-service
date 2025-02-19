# Adding a New Model to the ML Microservice

This guide explains how to add a new model to the microservice using the updated **dynamic model registration** approach. Each step is accompanied by explanations of the changes and why they are necessary.

---

## 1. Update `models_config.json`

The `models_config.json` file contains the configuration for all models. To add a new model:

1. Open the `models_config.json` file.
2. Add a new entry for your model. Ensure each model has a unique ID, correct file path, and type.

**Example:**
```json
{
    "models": [
        {
            "id": "model_a",
            "path": "app/models/model_a.pkl",
            "type": "sklearn"
        },
        {
            "id": "model_b",
            "path": "app/models/model_b.pkl",
            "type": "numerical"
        },
        {
            "id": "model_c",
            "path": "app/models/model_c.pkl",
            "type": "custom"
        }
    ]
}
```

**Why?**
- This ensures models are dynamically registered at startup without modifying the code.
- Centralizes model configurations for better maintainability.

---

## 2. Create or Update Preprocessor

Each model type requires a preprocessor to handle input transformations. If the new model type is not already supported:

1. Create a new preprocessor class in `app/preprocessors`.
2. Extend `BasePreprocessor` and implement the `preprocess` method.

**Example: `custom_preprocessor.py`**
```python
from app.preprocessors.base_preprocessor import BasePreprocessor
from app.logger import get_logger

logger = get_logger(__name__)

class CustomPreprocessor(BasePreprocessor):
    def preprocess(self, input_data):
        logger.info(f"Preprocessing input data: {input_data}")

        # Example preprocessing for custom model
        text = input_data.get("text")
        if not text:
            raise ValueError("The 'text' field is missing or None.")
        
        # Perform masking or transformations
        masked_text = self.mask_input(text)
        return {"features": [masked_text]}
    
    def mask_input(self, text):
        # Example masking function
        import re
        return re.sub(r"\\d", "*", text)
```

**Why?**
- Preprocessors standardize and validate inputs before they are passed to the model.

---

## 3. Create or Update Postprocessor

Each model type requires a postprocessor to handle output transformations. If the new model type is not already supported:

1. Create a new postprocessor class in `app/postprocessors`.
2. Extend `BasePostprocessor` and implement the `postprocess` method.

**Example: `custom_postprocessor.py`**
```python
from app.postprocessors.base_postprocessor import BasePostprocessor
from app.logger import get_logger

logger = get_logger(__name__)

class CustomPostprocessor(BasePostprocessor):
    def postprocess(self, raw_prediction):
        logger.info(f"Postprocessing raw prediction: {raw_prediction}")
        
        # Example transformation
        if not isinstance(raw_prediction, list):
            raise ValueError("Raw prediction must be a list.")
        return f"Processed custom result: {raw_prediction}"
```

**Why?**
- Postprocessors ensure model outputs are formatted and human-readable.

---

## 4. Update `ProcessorRegistry`

Register the new preprocessor and postprocessor in `app/config/registry.py`.

**Example:**
```python
from app.preprocessors.custom_preprocessor import CustomPreprocessor
from app.postprocessors.custom_postprocessor import CustomPostprocessor

class ProcessorRegistry:
    _preprocessors = {
        "sklearn": SklearnPreprocessor,
        "numerical": NumericalPreprocessor,
        "custom": CustomPreprocessor,
    }

    _postprocessors = {
        "sklearn": SklearnPostprocessor,
        "numerical": NumericalPostprocessor,
        "custom": CustomPostprocessor,
    }
```

**Why?**
- This step maps model types to their corresponding preprocessor and postprocessor.

---

## 5. Train or Provide the Model

1. Train the model or ensure the `.pkl` file is available at the specified `path` in `models_config.json`.
2. Save the model using libraries like `pickle`.

**Example (if creating a new model):**
```python
import pickle

# Example model
model = SomeMLModel()
model.fit(X_train, y_train)

with open("app/models/model_c.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved at app/models/model_c.pkl")
```

**Why?**
- The microservice depends on the serialized `.pkl` file to load models dynamically.

---

## 6. Update Tests

Add test cases to validate the new model in `app/tests/test_prediction.py`.

**Example:**
```python
def test_custom_model_prediction(client):
    response = client.post("/predict/model_c", json={"input": "Sample text"})
    assert response.status_code == 200
    assert "Processed custom result" in response.json()["prediction"]
```

**Why?**
- Ensure the new model integration works correctly with the microservice.

---

## 7. Test the Microservice

Use `curl` or a REST client like Postman to test the new model:

**Example Request:**
```bash
curl --location 'http://127.0.0.1:8000/predict/model_c' \\
--header 'Content-Type: application/json' \\
--data '{"input": "Sample input text"}'
```

**Expected Response:**
```json
{
    "prediction": "Processed custom result: ..."
}
```

---

## Summary of Benefits

1. **Dynamic Registration**:
   - Adding new models only requires changes to `models_config.json`.
   - Reduces the risk of missing updates in code.

2. **Preprocessor and Postprocessor**:
   - Decouples input/output logic from core services.
   - Ensures data consistency and security (e.g., masking sensitive data).

3. **Scalability**:
   - Easily add multiple models of different types.
   - Supports a wide range of use cases (text, numerical, custom).

4. **Code Reusability**:
   - Preprocessors and postprocessors are reusable components for similar models.

By following this guide, you can efficiently add new models with minimal changes to the microservice.
"""