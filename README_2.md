
# ML Microservice Documentation

This project is a production-grade microservice for serving predictions from an ML model using FastAPI. It is designed with best practices such as logging, exception handling, modular structure, and scalability.

---

## **Contents**

1. [Overview](#overview)
2. [Folder Structure](#folder-structure)
3. [Getting Started](#getting-started)
4. [FAQs](#faqs)
5. [Additional Resources](#additional-resources)

---

## **Overview**

The microservice provides a REST API to:
1. Serve predictions from a pre-trained ML model.
2. Perform health checks to ensure the service is running.
3. Validate user inputs using Pydantic.
4. Log detailed information for debugging and monitoring.

---

## **Folder Structure**

```
ml_microservice/
├── app/
│   ├── __init__.py             # Initializes the app package
│   ├── main.py                 # Entry point for the FastAPI application
│   ├── config.py               # Manages environment variables and configurations
│   ├── logger.py               # Configures logging across the application
│   ├── exceptions.py           # Custom exception handling classes
│   ├── models/                 # Model-related files
│   │   ├── __init__.py
│   │   ├── model_loader.py     # Loads the serialized ML model
│   │   └── model.pkl           # Serialized ML model file
│   ├── schemas.py              # Input validation schemas
│   ├── services/               # Business logic for predictions
│   │   ├── __init__.py
│   │   └── prediction_service.py  # Handles prediction logic
│   └── utils/                  # Helper utilities
│       ├── __init__.py
│       └── helpers.py          # Miscellaneous utility functions
│
├── tests/                      # Unit and integration tests
│   ├── __init__.py
│   ├── test_main.py            # Tests for API endpoints
│   ├── test_prediction_service.py  # Tests for prediction logic
│   └── fixtures/               # Sample test data fixtures
│       ├── __init__.py
│       └── sample_input.json   # Example input for testing
│
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Dockerfile for containerizing the service
├── .env                        # Environment variables for configurations
├── .gitignore                  # Ignored files for version control
└── README.md                   # Documentation
```

For detailed descriptions of each file, refer to the [File Descriptions README](./docs/File_Descriptions.md).

---

## **Getting Started**

Follow the steps below to set up and run the microservice:

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

4. **Generate a Sample ML Model**:
   ```bash
   python app/models/model_generator.py
   ```

5. **Run the Service**:
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the Endpoints**:
   - Health Check: `http://127.0.0.1:8000/health`
   - Prediction: `POST http://127.0.0.1:8000/predict`

---

## **FAQs**

Frequently Asked Questions about this microservice can be found [here](./docs/FAQs.md).

---

## **Additional Resources**

1. [Detailed File Descriptions](./docs/File_Descriptions.md)
2. [API Endpoints Guide](./docs/API_Endpoints.md)
3. [Development and Deployment Guide](./docs/Deployment_Guide.md)

For further assistance, feel free to reach out!
