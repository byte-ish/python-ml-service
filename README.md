
# Python ML Microservice

## Overview

This project is a Python-based microservice designed to demonstrate machine learning (ML) integration with RESTful APIs using FastAPI. The service provides endpoints for liveliness checks and ML model predictions. It is structured for scalability, performance, and adherence to industry standards.

---

## Features

- **RESTful Endpoints**:
  - `GET /healthcheck`: Liveliness and health check.
  - `POST /predict`: Accepts input, processes it through an ML model, and returns predictions.

- **Machine Learning**:
  - Uses a Logistic Regression model from `scikit-learn`.
  - Mock training is implemented for simplicity, but the model can be replaced with a pre-trained or custom model.

- **Project Structure**:
  - Modular design following best practices for maintainability and scalability.
  - Separate layers for routes, services, and models.

- **Testing**:
  - Unit tests for critical functionality using `pytest`.

- **Containerization**:
  - Fully containerized using Docker with a lean Dockerfile for optimized deployment.

---

## Project Structure

```
microservice/
├── app/
│   ├── __init__.py
│   ├── main.py                # Entry point for the FastAPI app
│   ├── models/                # ML model logic
│   │   ├── __init__.py
│   │   └── ml_model.py        # Model loading and prediction
│   ├── routes/                # API route handlers
│   │   ├── __init__.py
│   │   ├── healthcheck.py     # Healthcheck endpoint
│   │   └── prediction.py      # Prediction endpoint
│   ├── services/              # Business logic for the API
│   │   ├── __init__.py
│   │   └── prediction_service.py
│   ├── tests/                 # Unit tests
│   │   ├── __init__.py
│   │   ├── test_healthcheck.py
│   │   └── test_prediction.py
├── Dockerfile                 # Container configuration
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
```

---

## Endpoints

### **1. Healthcheck**
**Description**: Checks the service's liveliness and readiness.

- **Method**: `GET`
- **URL**: `/healthcheck`

#### Example Request:
```bash
curl -X GET http://localhost:8000/healthcheck
```

#### Example Response:
```json
{
  "status": "healthy"
}
```

---

### **2. Prediction**
**Description**: Accepts input and returns a prediction using the ML model.

- **Method**: `POST`
- **URL**: `/predict`
- **Body**:
  - `value` (float): Input value for the prediction.

#### Example Request:
```bash
curl -X POST http://localhost:8000/predict      -H "Content-Type: application/json"      -d '{"value": 2.0}'
```

#### Example Response:
```json
{
  "prediction": [1]
}
```

---

## Setup Instructions

### **1. Prerequisites**
- Python 3.9 or higher
- `pip` (Python package manager)
- Docker (optional, for containerization)

---

### **2. Installation**

#### Clone the Repository:
```bash
git clone <repository-url>
cd microservice
```

#### Install Dependencies:
```bash
pip install -r requirements.txt
```

---

### **3. Run the Application**

#### Run Locally:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

#### Run with Docker:
1. Build the Docker Image:
   ```bash
   docker build -t python-microservice .
   ```

2. Run the Container:
   ```bash
   docker run -p 8000:8000 python-microservice
   ```

---

### **4. Testing**

Run unit tests using `pytest`:
```bash
pytest app/tests/
```

---

## Development Guide

### **Adding a New Endpoint**
1. Create a new file in the `routes/` directory.
2. Define the endpoint logic.
3. Register the route in `main.py`.

### **Modifying the ML Model**
1. Update the `train_mock_model()` function in `ml_model.py`.
2. Replace or extend `predict_with_model()` for custom prediction logic.

---

## Deployment Guide

1. Build the Docker image:
   ```bash
   docker build -t python-microservice .
   ```

2. Push to a container registry (e.g., DockerHub):
   ```bash
   docker tag python-microservice <your-dockerhub-username>/python-microservice
   docker push <your-dockerhub-username>/python-microservice
   ```

3. Deploy using orchestration tools like Kubernetes, Docker Swarm, or ECS.

---

## Future Enhancements

- Add logging and monitoring.
- Integrate with a database for stateful operations.
- Replace mock model training with a production-grade ML pipeline.
- Integrate OpenTelemetry for observability.

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
