"""
# Directory Structure of the ML Model Microservice

This document provides a detailed overview of the directory structure of the ML Model Microservice. Each folder and file is explained thoroughly, helping new developers or users understand its purpose and functionality.

---

## Root Structure

```
ml-microservice/
│
├── app/                   # Core application package
│   ├── config/            # Configuration and registry modules
│   ├── models/            # Model-related logic and files
│   ├── preprocessors/     # Preprocessing logic for input data
│   ├── postprocessors/    # Postprocessing logic for model outputs
│   ├── routes/            # API route handlers
│   ├── schemas/           # Request and response validation schemas
│   ├── services/          # Core services (e.g., prediction service)
│   ├── utils/             # Utility modules (e.g., logging, JWT, metrics)
│   ├── __init__.py        # Marks the app directory as a package
│   ├── exceptions.py      # Custom exceptions for error handling
│   └── main.py            # Entry point of the application
│
├── tests/                 # Unit tests for all components
│   ├── test_config.py     # Tests for configuration logic
│   ├── test_models.py     # Tests for model-related components
│   ├── ...                # Other test files
│
├── .env.development       # Environment variables for development
├── .env.staging           # Environment variables for staging
├── .env.production        # Environment variables for production
├── pytest.ini             # Configuration for pytest
├── requirements.txt       # List of required Python dependencies
├── README.md              # Comprehensive project documentation
└── ...                    # Additional files (e.g., Dockerfile, CI/CD scripts)
```

---

## Detailed Breakdown

### `app/`
The main application directory containing all core components of the microservice.

#### `config/`
- **Purpose**: Manage application settings and model registry.
- **Key Files**:
  - `config.py`: Loads environment variables and settings.
  - `registry.py`: Maps models to their preprocessors and postprocessors.

#### `models/`
- **Purpose**: Handle all logic related to machine learning models.
- **Key Files**:
  - `model_registry.py`: Central registry for managing models and configurations.
  - `model_loader.py`: Logic to dynamically load models from disk.
  - `mock_string_model.py`: Mock model for testing string inputs and outputs.
  - `model_generator.py`: Script to generate and save mock models.

#### `preprocessors/`
- **Purpose**: Preprocess raw input data before passing it to models.
- **Key Files**:
  - `base_preprocessor.py`: Abstract base class defining the preprocessing interface.
  - `sklearn_preprocessor.py`: Preprocessor for sklearn-based models.
  - `numerical_preprocessor.py`: Preprocessor for numerical models.

#### `postprocessors/`
- **Purpose**: Format raw model outputs into user-friendly responses.
- **Key Files**:
  - `base_postprocessor.py`: Abstract base class defining the postprocessing interface.
  - `sklearn_postprocessor.py`: Postprocessor for sklearn-based models.
  - `numerical_postprocessor.py`: Postprocessor for numerical models.

#### `routes/`
- **Purpose**: Define the API endpoints.
- **Key Files**:
  - `healthcheck.py`: Health check endpoint to verify service status.
  - `prediction.py`: Endpoint for making predictions using models.
  - `auth.py`: Endpoint for authentication (e.g., Jira login).

#### `schemas/`
- **Purpose**: Validate and define the structure of API requests and responses.
- **Key Files**:
  - `prediction_schema.py`: Schemas for prediction requests and responses.
  - `common_schema.py`: Shared schemas for common data structures.

#### `services/`
- **Purpose**: Business logic and service-layer functionality.
- **Key Files**:
  - `prediction_service.py`: Core logic for handling prediction requests.

#### `utils/`
- **Purpose**: Provide shared utility functions and classes.
- **Key Files**:
  - `logger.py`: Implements structured JSON logging with contextual information.
  - `jwt.py`: Functions for creating and verifying JWT tokens.
  - `metrics.py`: Prometheus metrics for monitoring the microservice.

#### Other Files in `app/`
- `exceptions.py`: Custom exception classes for better error handling.
- `main.py`: Entry point of the application. Initializes the FastAPI app, middleware, and routes.

---

### `tests/`
- **Purpose**: Contains unit tests for all components of the microservice.
- **Key Files**:
  - `test_config.py`: Tests configuration settings and environment loading.
  - `test_models.py`: Tests for model registry, loader, and related logic.
  - `test_routes.py`: Tests for API endpoints.
  - `test_utils.py`: Tests for utility functions (e.g., JWT creation, logging).

---

### Environment Files (`.env.*`)
- **Purpose**: Define environment-specific variables for configuration.
- **Key Files**:
  - `.env.development`: Variables for local development.
  - `.env.staging`: Variables for staging environment.
  - `.env.production`: Variables for production deployment.

---

### `pytest.ini`
- **Purpose**: Configuration for `pytest`, including test discovery rules and coverage settings.

---

### `requirements.txt`
- **Purpose**: List of Python libraries required to run the microservice.
- **Example Dependencies**:
  - `fastapi`: Framework for building APIs.
  - `scikit-learn`: ML library for models.
  - `pydantic`: Validation and data modeling.

---

### `README.md`
- **Purpose**: Provides an overview of the project and its usage.
- **Contents**:
  - Quick Start Guide
  - Key Features
  - Directory Structure
  - Adding New Models
  - Monitoring and Metrics
  - Testing Instructions

---

## Adding a New File or Feature

1. **Decide the Purpose**: Determine the purpose of the new feature or file.
2. **Select the Directory**: Place the file in the appropriate directory (e.g., preprocessors for input preprocessing logic).
3. **Write Tests**: Ensure the new feature is covered by unit tests in the `tests/` directory.
4. **Update Documentation**: Add details about the new feature in the relevant documentation files (e.g., `README.md`, `features.md`).

---

Move to the next section for a step-by-step guide on [executing the project](docs/execution_guide.md).
