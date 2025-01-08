
# API Endpoints Guide

This document provides details about the available API endpoints in the microservice.

---

## **Endpoints**

### **1. Health Check**
- **Path**: `/health`
- **Method**: `GET`
- **Description**: Checks if the service is running.
- **Example Request**:
  ```bash
  curl http://127.0.0.1:8000/health
  ```
- **Response**:
  ```json
  {
      "status": "ok",
      "message": "Service is running"
  }
  ```

---

### **2. Prediction**
- **Path**: `/predict`
- **Method**: `POST`
- **Description**: Accepts input data and returns predictions from the ML model.
- **Request Body**:
  ```json
  {
      "features": [5.1, 3.5, 1.4, 0.2]
  }
  ```
- **Example Request**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/predict"   -H "Content-Type: application/json"   -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
  ```
- **Response**:
  ```json
  {
      "prediction": [0]
  }
  ```
  - **Note**: The prediction is a numerical class label corresponding to the trained model's output.

---

For additional details, refer to the [Development and Deployment Guide](Deployment_Guide.md).
