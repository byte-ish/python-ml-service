
# File Descriptions

This document provides detailed descriptions of each file in the project.

---

## **Main Files**

1. **`app/main.py`**:
   - The entry point for the FastAPI application.
   - Defines the REST API endpoints for health checks and predictions.

2. **`app/config.py`**:
   - Manages environment variables using `python-dotenv`.
   - Provides centralized configuration for model paths, logging levels, etc.

3. **`app/logger.py`**:
   - Configures logging for the entire application.
   - Ensures consistent log formatting and supports different log levels.

4. **`app/exceptions.py`**:
   - Contains custom exception classes to handle predictable errors, such as model loading failures.

5. **`app/models/model_loader.py`**:
   - Loads the serialized ML model (`model.pkl`) at runtime.
   - Raises a `ModelNotFoundError` if the model file is missing.

6. **`app/schemas.py`**:
   - Defines Pydantic schemas for validating API inputs.

7. **`app/services/prediction_service.py`**:
   - Contains the logic to make predictions using the loaded ML model.
   - Handles input preprocessing and exception handling.

---

## **Test Files**

1. **`tests/test_main.py`**:
   - Contains tests for API endpoints, including health checks and predictions.

2. **`tests/test_prediction_service.py`**:
   - Tests the business logic for predictions.

3. **`tests/fixtures/sample_input.json`**:
   - Provides example inputs for tests, ensuring reproducibility.

---

For further questions, refer to the [FAQs](./FAQs.md).
