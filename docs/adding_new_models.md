"""
# Adding New Models

This guide provides a step-by-step explanation for adding new models to the microservice. The goal is to ensure that even individuals with minimal experience in Python or Machine Learning can follow the instructions effectively.

---

## Overview

Adding new models to the microservice allows it to handle additional tasks or datasets. Each model should have its preprocessing and postprocessing logic to ensure compatibility with the microservice's input and output formats.

---

## Steps to Add a New Model

### 1. **Prepare Your Model**
   - Train your model using a framework such as Scikit-Learn, TensorFlow, or PyTorch.
   - Save the trained model to a file in the appropriate format:
     - For Scikit-Learn, save the model using the `pickle` or `joblib` library.
     - For other frameworks, use their respective serialization formats (e.g., `.h5` for TensorFlow).

   **Example**: Save a Scikit-Learn model:
   ```python
   import pickle
   from sklearn.ensemble import RandomForestClassifier

   model = RandomForestClassifier()
   # Train your model here
   with open("app/models/new_model.pkl", "wb") as file:
       pickle.dump(model, file)
   ```

   - Place the model file in the `app/models` directory.

---

### 2. **Update the `models_config.json` File**
   - The `models_config.json` file contains metadata about all registered models.
   - Add a new entry to the configuration file with the following details:
     - **id**: A unique identifier for the model.
     - **path**: The file path to the model.
     - **type**: The type of the model (e.g., `sklearn`, `numerical`).

   **Example**:
   ```json
   {
       "models": [
           {
               "id": "new_model",
               "path": "app/models/new_model.pkl",
               "type": "sklearn"
           }
       ]
   }
   ```

   - Ensure that the `path` matches the location of your saved model file.

---

### 3. **Add Preprocessing Logic**
   - Define how the input data should be transformed for the new model.
   - Add a new preprocessor class in the `app/preprocessors` directory.

   **Example**: A preprocessor for a text-based model:
   ```python
   from app.preprocessors.base_preprocessor import BasePreprocessor

   class NewModelPreprocessor(BasePreprocessor):
       def preprocess(self, input_data):
           text = input_data.get("input")
           if not isinstance(text, str):
               raise ValueError("Input must be a string.")
           return {"features": [text.lower()]}
   ```

   - Update the `ProcessorRegistry` in `app/config/registry.py` to include your preprocessor:
   ```python
   _preprocessors = {
       "sklearn": SklearnPreprocessor,
       "numerical": NumericalPreprocessor,
       "new_model_type": NewModelPreprocessor,
   }
   ```

---

### 4. **Add Postprocessing Logic**
   - Define how the model's raw output should be processed.
   - Add a new postprocessor class in the `app/postprocessors` directory.

   **Example**: A postprocessor for a numerical model:
   ```python
   from app.postprocessors.base_postprocessor import BasePostprocessor

   class NewModelPostprocessor(BasePostprocessor):
       def postprocess(self, prediction):
           return f"Processed: {prediction}"
   ```

   - Update the `ProcessorRegistry` in `app/config/registry.py` to include your postprocessor:
   ```python
   _postprocessors = {
       "sklearn": SklearnPostprocessor,
       "numerical": NumericalPostprocessor,
       "new_model_type": NewModelPostprocessor,
   }
   ```

---

### 5. **Test Your Model**
   - Ensure that your model is functioning correctly by running unit tests.
   - Add tests for preprocessing, postprocessing, and prediction in the `tests` directory.

   **Example**:
   ```python
   def test_new_model_preprocessing():
       preprocessor = NewModelPreprocessor()
       input_data = {"input": "Hello World"}
       processed_data = preprocessor.preprocess(input_data)
       assert processed_data == {"features": ["hello world"]}
   ```

   - Use `pytest` to run your tests:
   ```bash
   pytest --cov=app tests/
   ```

---

## Troubleshooting

1. **Model Not Found**
   - Ensure that the model file exists at the specified path in `models_config.json`.

2. **Preprocessing Errors**
   - Verify that the input data matches the expected format for your preprocessor.

3. **Postprocessing Errors**
   - Check that the raw prediction output from the model aligns with the logic in your postprocessor.

4. **Prediction Endpoint Fails**
   - Ensure that the model ID matches the ID in `models_config.json`.

---

By following these steps, you can add new models to the microservice and extend its capabilities. Ensure thorough testing to validate the integration of your new model.
"""