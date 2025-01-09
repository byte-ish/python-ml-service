# Features of the ML Model Microservice

The **ML Model Microservice** is a robust and feature-rich service designed to simplify the deployment and usage of machine learning models in production environments. It provides extensive support for API-based inference, model management, authentication, logging, monitoring, and more.

---

## Key Features

### 1. **RESTful API**
- **Endpoints**: Provides well-documented RESTful endpoints for prediction, health checks, and authentication.
- **FastAPI Framework**: Built using FastAPI for asynchronous, high-performance API handling.
- **Extensibility**: Easily extendable with new endpoints and functionality.

---

### 2. **Model Inference**
- **Multi-Model Support**: Handles text-based models (e.g., `sklearn`) and numerical models (e.g., neural networks).
- **Dynamic Loading**: Models are loaded dynamically based on the provided configuration.
- **Custom Preprocessors and Postprocessors**:
  - **Preprocessors**: Process input data based on the model type (e.g., text cleaning or numerical transformations).
  - **Postprocessors**: Format model output into a user-friendly response.

---

### 3. **Model Registry**
- **Centralized Configuration**: Models and their metadata (e.g., ID, path, type) are centrally managed in a JSON configuration file.
- **Caching Mechanism**: Avoids reloading models multiple times by caching them in memory.
- **Validation**: Ensures model paths and types are correct during registration.

---

### 4. **Authentication**
- **Jira Integration**: Supports authentication using Jira credentials (email and API token).
- **JWT Tokens**:
  - Issues secure JSON Web Tokens (JWT) for authenticated users.
  - Provides configurable token expiration times and algorithms.
- **Security**: Prevents unauthorized access to prediction endpoints.

---

### 5. **Health Check**
- **Real-Time Status**: Provides a `/health` endpoint to check the service's operational status.
- **Detailed Information**: Returns the version and status of the service.

---

### 6. **Logging**
- **Structured JSON Logs**:
  - Includes details like timestamp, log level, request ID, and message.
  - Logs are formatted into JSON for seamless integration with log aggregation tools.
- **Contextual Logging**:
  - Automatically associates logs with a unique request ID for traceability.
  - Includes stack traces for unexpected errors.
- **Log Rotation**:
  - Prevents disk usage issues by rotating log files after they exceed a configured size.

---

### 7. **Monitoring and Metrics**
- **Prometheus Integration**:
  - Provides metrics for monitoring API performance and behavior.
  - Includes custom metrics like prediction endpoint hits and response times.
- **Histogram Buckets**: Configurable buckets for latency distribution tracking.

---

### 8. **Testing**
- **Comprehensive Unit Tests**:
  - Tests for all core functionalities, including model inference, authentication, and schema validation.
  - Uses `pytest` and `pytest-cov` for writing and measuring test coverage.
- **Mocking and Patching**:
  - Simulates model behavior and external API calls for isolated testing.
- **High Coverage**: Aims for 90%+ test coverage to ensure reliability.

---

### 9. **Extensibility**
- **Adding New Models**:
  - Easily register and configure new models through the `models_config.json` file.
  - Supports custom preprocessing and postprocessing logic for each model type.
- **Adding New Endpoints**:
  - Modular route definitions make it simple to extend the API.

---

### 10. **Configuration**
- **Environment-Based Settings**:
  - Supports separate `.env` files for development, staging, and production environments.
- **Customizable Parameters**:
  - Model paths, API keys, and logging levels can be easily modified.

---

### 11. **Error Handling**
- **Standardized Responses**:
  - Provides consistent error responses for easier debugging.
  - Includes request IDs in errors for traceability.
- **Custom Exceptions**:
  - Handles specific issues like prediction failures and service errors with custom exceptions.

---

## Why Use This Microservice?

This microservice is designed to provide a seamless interface between machine learning models and real-world applications. Its robust feature set ensures:
- **Scalability**: Ready for deployment in production environments.
- **Ease of Use**: Simplifies model integration and API usage.
- **Reliability**: Built-in testing, monitoring, and error handling for high reliability.
- **Extensibility**: Easily adapt the service to meet evolving business needs.

---

Move to the next section for a detailed explanation of the [directory structure](directory_structure.md).