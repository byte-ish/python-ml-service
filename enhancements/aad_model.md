"""
# Adding a New ML Model to the Microservice

This guide explains the step-by-step process to integrate a new machine learning (ML) model into the existing microservice. Each step includes an explanation of its relevance.

---

## Steps to Add a New Model

### 1. **Prepare the Model**
   - Train and export the ML model in a compatible format (e.g., `.pkl` for Python models).
   - Place the model file in the appropriate directory, e.g., `app/models/`.

   **Why?**  
   The microservice requires a serialized model file that can be dynamically loaded during inference.

---

### 2. **Register the Model**
   Update the model registration logic in `main.py` under the `startup_event` function:

   ```python
   from app.models.model_registry import ModelRegistry

   @app.on_event("startup")
   async def startup_event():
       ModelRegistry.register_model("new_model", "app/models/new_model.pkl")
   ```

   **Why?**  
   Registration maps the model ID to its file path and allows the microservice to load the model dynamically.

---

### 3. **Add Preprocessor and Postprocessor**
   - Implement custom preprocessing and postprocessing logic for the new model:
     - **Preprocessor:** Add a class in `app/preprocessors/` (e.g., `new_model_preprocessor.py`).
     - **Postprocessor:** Add a class in `app/postprocessors/` (e.g., `new_model_postprocessor.py`).

   Example:
   ```python
   # app/preprocessors/new_model_preprocessor.py
   from app.preprocessors.base_preprocessor import BasePreprocessor

   class NewModelPreprocessor(BasePreprocessor):
       def preprocess(self, input_data: dict) -> dict:
           # Custom preprocessing logic
           return {"features": input_data["text"]}
   ```

   ```python
   # app/postprocessors/new_model_postprocessor.py
   from app.postprocessors.base_postprocessor import BasePostprocessor

   class NewModelPostprocessor(BasePostprocessor):
       def postprocess(self, prediction):
           # Custom postprocessing logic
           return {"result": prediction}
   ```

   **Why?**  
   These classes handle input transformations and format the model's raw output into a user-friendly format.

---

### 4. **Update the Registry**
   Update the `ProcessorRegistry` in `app/config/registry.py` to include the new preprocessor and postprocessor:

   ```python
   from app.preprocessors.new_model_preprocessor import NewModelPreprocessor
   from app.postprocessors.new_model_postprocessor import NewModelPostprocessor

   PROCESSORS = {
       "new_model": {
           "preprocessor": NewModelPreprocessor,
           "postprocessor": NewModelPostprocessor,
       },
   }
   ```

   **Why?**  
   The registry dynamically selects the appropriate preprocessor and postprocessor based on the model type.

---

### 5. **Update Request and Response Schemas**
   If the new model requires specific input or output formats, update or add new schemas in `app/schemas.py`:

   ```python
   class NewModelInput(BaseModel):
       text: str = Field(..., description="Input text for the new model.")

   class NewModelResponse(BaseModel):
       result: str = Field(..., description="Processed result from the new model.")
   ```

   **Why?**  
   Schemas ensure input validation and define the response structure.

---

### 6. **Test the Integration**
   - Write unit tests for the new preprocessor, postprocessor, and model inference.
   - Example test for the preprocessor:
     ```python
     def test_new_model_preprocessor():
         preprocessor = NewModelPreprocessor()
         result = preprocessor.preprocess({"text": "Test input"})
         assert "features" in result
     ```

   **Why?**  
   Comprehensive tests verify the correctness of the new implementation and prevent future regressions.

---

### 7. **Test API Endpoints**
   Use `curl` or Postman to test the `/predict` endpoint with the new model:

   Example `curl` request:
   ```bash
   curl --location 'http://127.0.0.1:8000/predict/new_model' \
   --header 'Authorization: Bearer <JWT_TOKEN>' \
   --header 'Content-Type: application/json' \
   --data '{"text": "Sample input for new model"}'
   ```

   **Why?**  
   End-to-end testing ensures the model is correctly integrated with the API.

---

### 8. **Document the Model**
   - Add details about the new model in the project documentation:
     - Input and output formats.
     - Example requests and responses.
   - Update the OpenAPI documentation with new schemas and examples.

   **Why?**  
   Clear documentation helps developers and users understand how to interact with the service.

---

### Summary
By following these steps, you can seamlessly integrate a new ML model into the microservice, ensuring modularity, scalability, and maintainability.
"""