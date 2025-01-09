# Frequently Asked Questions (FAQ)

This FAQ document addresses common questions and challenges you might encounter while working with the **ML Model Microservice**. If you have additional questions, feel free to extend this file or reach out for support.

---

## Table of Contents
1. [General Questions](#general-questions)
2. [Setup and Execution](#setup-and-execution)
3. [Adding New Models](#adding-new-models)
4. [Testing and Coverage](#testing-and-coverage)
5. [Monitoring and Metrics](#monitoring-and-metrics)
6. [Troubleshooting](#troubleshooting)

---

## General Questions

### 1. What is the purpose of this microservice?
The **ML Model Microservice** is designed to provide a modular and scalable framework for:
- **Serving ML models** through RESTful endpoints.
- **Preprocessing** and **postprocessing** model inputs and outputs.
- **Monitoring** application performance via Prometheus metrics.
- Ensuring high **code quality** with structured error handling and testing.

### 2. Who is this microservice for?
This microservice is ideal for developers and teams looking to:
- Deploy ML models as scalable APIs.
- Maintain high code quality and structured logging.
- Monitor application metrics for performance insights.

---

## Setup and Execution

### 1. How do I install the required dependencies?
To install all dependencies, run:
```bash
pip install -r requirements.txt
```
Refer to the [Setup and Execution Guide](setup_and_execution.md) for detailed steps.

### 2. Can I run this service on Windows/Mac/Linux?
Yes, the microservice is platform-independent. It runs wherever Python 3.10 or higher is supported.

### 3. How do I start the service locally?
Run the following command:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
For detailed instructions, refer to the [Setup and Execution Guide](setup_and_execution.md).

---

## Adding New Models

### 1. How do I add a new model?
Follow these steps:
1. Update the `models_config.json` file with the new model's details.
2. Place the model file in the appropriate directory.
3. Ensure preprocessors and postprocessors for the new model type are implemented.

Refer to the [Adding New Models Guide](adding_new_models.md) for a step-by-step walkthrough.

### 2. What are the supported model types?
Currently, the service supports:
- **`sklearn` models** for text-based input/output.
- **`numerical` models** for list-based numerical data.

To add support for new types, implement the required preprocessor and postprocessor classes.

---

## Testing and Coverage

### 1. How do I run the tests?
Run all tests and generate a coverage report with:
```bash
pytest --cov=app tests/
```
For more details, refer to the [Testing Guide](testing.md).

### 2. How do I achieve higher test coverage?
Ensure that all classes, methods, and edge cases are covered by:
- Writing unit tests for untested methods.
- Testing exception-handling scenarios.
- Validating both valid and invalid inputs.

### 3. Why is a specific test failing?
Check the test failure log and:
- Verify that the input and output align with the function's requirements.
- Ensure the correct mock objects are used for dependencies.
- Look for typos or incorrect configurations in the `tests` directory.

---

## Monitoring and Metrics

### 1. What metrics are available?
This service exposes:
- **Request counts** for prediction endpoints (`PREDICTION_HIT_COUNTER`).
- **Response time** histograms for prediction requests (`PREDICTION_RESPONSE_TIME`).

### 2. How do I view metrics?
Metrics are exposed at `/metrics` and can be integrated with Prometheus/Grafana. Refer to the [Monitoring and Metrics Guide](monitoring_and_metrics.md) for setup details.

---

## Troubleshooting

### 1. The application doesn't start. What should I do?
Check the following:
- Ensure Python 3.10+ is installed.
- Verify that dependencies are installed by running `pip install -r requirements.txt`.
- Check the logs for errors when starting the application.

### 2. A model is not being recognized. What might be wrong?
- Ensure the model is registered in `models_config.json`.
- Verify the file path and model type.
- Check for typos in the `model_id`.

### 3. I'm seeing a 500 error when calling the `/predict` endpoint.
This usually indicates an internal issue. Steps to debug:
1. Verify the input format matches the model type.
2. Check the logs for detailed error messages.
3. Ensure the preprocessor and postprocessor for the model type are correctly implemented.

### 4. How do I debug issues in production?
- Use the structured JSON logs saved to `app_logs.log`.
- Monitor metrics via Prometheus/Grafana.
- Test individual components in isolation (e.g., preprocessors, postprocessors, model loading).

---

If your question isn't listed here, feel free to extend this FAQ or refer to the relevant documentation files listed in the [Table of Contents](#table-of-contents).

---