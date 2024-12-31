
# Development and Deployment Guide

This guide provides instructions for running, testing, and deploying the microservice.

---

## **Development**

### **Set Up the Environment**

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd ml_microservice
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3.10 -m venv ml_microservice_env
   source ml_microservice_env/bin/activate  # macOS/Linux
   ml_microservice_env\Scripts\activate   # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Testing**

1. **Run Tests**:
   - Install `pytest` if not already installed:
     ```bash
     pip install pytest
     ```
   - Run the tests:
     ```bash
     pytest tests/
     ```

2. **Test Coverage**:
   - Install `pytest-cov`:
     ```bash
     pip install pytest-cov
     ```
   - Generate a coverage report:
     ```bash
     pytest --cov=app tests/
     ```

---

## **Deployment**

### **Docker Deployment**

1. **Build the Docker Image**:
   ```bash
   docker build -t ml-microservice .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -p 8000:8000 ml-microservice
   ```

3. **Access the Service**:
   - Health Check: `http://127.0.0.1:8000/health`
   - Prediction: `POST http://127.0.0.1:8000/predict`

---

### **Cloud Deployment**

1. **AWS ECS or Fargate**:
   - Push the Docker image to AWS ECR (Elastic Container Registry).
   - Deploy the container using ECS or Fargate.

2. **Kubernetes**:
   - Create a Kubernetes deployment and service configuration.
   - Deploy the container to a Kubernetes cluster.

---

For detailed cloud deployment instructions, refer to the cloud provider's documentation.
