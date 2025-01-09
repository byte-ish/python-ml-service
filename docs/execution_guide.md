"""
# How to Execute the Project

This guide provides step-by-step instructions for setting up and running the ML microservice. Follow these steps carefully, even if you are a complete beginner in Python or Machine Learning.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Running the Application](#running-the-application)
4. [Testing the Application](#testing-the-application)
5. [Viewing API Documentation](#viewing-api-documentation)
6. [Accessing Metrics and Monitoring](#accessing-metrics-and-monitoring)
7. [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)

---

## Prerequisites

Before running the project, ensure you have the following:

1. **Python Installed**: Install Python 3.10 or later. [Download Python](https://www.python.org/downloads/).
   - Verify installation:
     ```bash
     python --version
     ```
2. **Package Manager (pip)**: Comes pre-installed with Python. Verify with:
   ```bash
   pip --version
     ```
3. **Virtual Environment Tool**:
   - Use `venv` (Python’s built-in tool) or `conda` for managing dependencies in an isolated environment.
4. **Git Installed**: To clone the project repository. [Download Git](https://git-scm.com/downloads).
5. **Dependencies Installed**: Install project requirements (explained in the next section).

---

## Project Setup

1. **Clone the Repository**:
   - Open a terminal or command prompt and run:
     ```bash
     git clone <repository_url>
     cd <repository_directory>
     ```

2. **Create a Virtual Environment**:
   - Using `venv`:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On macOS/Linux
     venv\\Scripts\\activate     # On Windows
     ```
   - Using `conda`:
     ```bash
     conda create --name ml_microservice_env python=3.10 -y
     conda activate ml_microservice_env
     ```

3. **Install Dependencies**:
   - Run the following command to install all required packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Verify dependencies are installed by running:
     ```bash
     pip list
     ```

4. **Setup Environment Variables**:
   - Configure the `.env` file based on your environment (`development`, `staging`, or `production`):
     - Copy the example `.env` file:
       ```bash
       cp .env.example .env.development
       ```
     - Open the file and edit the values (e.g., `MODEL_PATH`, `API_KEY`, `JWT_SECRET_KEY`).

---

## Running the Application

1. **Run the Server**:
   - Use the following command to start the FastAPI application:
     ```bash
     uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
     ```
   - Expected output:
     ```bash
     INFO:     Application startup: Loading model configurations.
     INFO:     All models registered successfully. Total models: X
     INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
     ```

2. **Access the Application**:
   - Open a browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Testing the Application

1. **Run Unit Tests**:
   - Execute all tests:
     ```bash
     pytest --cov=app tests/
     ```
   - Check the code coverage report:
     ```bash
     ---------- coverage: platform darwin, python 3.10.16-final-0 ----------
     Name                             Stmts   Miss  Cover
     -------------------------------------------------------------------
     app/main.py                         45      2    96%
     ...
     ```

2. **Test API Endpoints**:
   - Use tools like [Postman](https://www.postman.com/downloads/) or [cURL](https://curl.se/) to test endpoints.
   - Example using `curl`:
     ```bash
     curl -X GET http://127.0.0.1:8000/health
     ```

---

## Viewing API Documentation

FastAPI automatically generates API documentation.

1. **Swagger UI**:
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
   - Explore all API endpoints interactively.

2. **ReDoc**:
   - Open [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).
   - View a detailed API specification.

---

## Accessing Metrics and Monitoring

The application is instrumented with Prometheus for metrics collection.

1. **View Prometheus Metrics**:
   - Visit [http://127.0.0.1:8000/metrics](http://127.0.0.1:8000/metrics).
   - Example metrics:
     ```
     # HELP prediction_endpoint_hits Number of hits to the prediction endpoint
     # TYPE prediction_endpoint_hits counter
     prediction_endpoint_hits 10
     ```

2. **Integrate with Grafana**:
   - Set up Grafana and connect it to your Prometheus server for visualizing metrics.

---

## Common Issues and Troubleshooting

1. **Missing Dependencies**:
   - Error:
     ```bash
     ModuleNotFoundError: No module named 'httpx'
     ```
   - Solution:
     ```bash
     pip install -r requirements.txt
     ```

2. **Server Fails to Start**:
   - Error in logs:
     ```
     FileNotFoundError: [Errno 2] No such file or directory: 'app/config/models_config.json'
     ```
   - Solution:
     - Ensure the `models_config.json` file exists and is valid.

3. **Prediction Issues**:
   - Error in response:
     ```
     {"detail": "Model 'test_model' is not registered."}
     ```
   - Solution:
     - Verify the model ID and ensure it is registered in `models_config.json`.

"""