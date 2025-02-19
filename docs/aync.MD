# ML Model Microservice 🚀

## Overview

This microservice is designed to provide predictions using multiple ML models. It supports both **synchronous** and **asynchronous** inference. The service is built with **FastAPI**, ensuring high performance and extensibility.

Key features:

- **Multi-Model Support**: Dynamically load and serve multiple ML models.
- **Asynchronous Processing**: API requests can be queued and processed in the background.
- **Task Queue with In-Memory Storage**: Implements an efficient queue without Redis.
- **Structured Logging & Exception Handling**: Ensures robustness and easy debugging.
- **JWT Authentication & API Key Support**: Secures API requests.

---

## Architecture 🏧

### High-Level Flow:

1. **Sync Prediction**: The `/predict/{model_id}` endpoint processes requests in real time.
2. **Async Prediction**:
    - The `/predict-async/{model_id}` endpoint queues requests.
    - A worker continuously processes the queue.
    - Results are stored and can be fetched via `/results/{task_id}`.
3. **JIRA Integration**:
    - Queries JIRA using JQL.
    - Extracts relevant issue details.
    - Feeds issue descriptions into the model for prediction.

---

## How Asynchronous Processing Works ⚙️

- **Queue-Based Execution**: Incoming requests are enqueued and processed sequentially.
- **Task Storage**: A dictionary (acting as an in-memory database) tracks task states (`pending`, `completed`, `failed`).
- **Polling for Results**: Clients fetch prediction results via a separate endpoint.

### Task Lifecycle:

```plaintext
1. Client sends a request → Task is queued → Response contains a task_id.
2. Background worker processes tasks.
3. Client fetches results using task_id.
```

---

## Installation & Setup 🛠️

### 1. Clone the Repository:

```sh
git clone https://github.com/your-repo/ml-microservice.git
cd ml-microservice
```

### 2. Install Dependencies:

```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables:

Create a `.env` file in the root directory:

```ini
# Environment Configuration
ENVIRONMENT=development
LOG_LEVEL=INFO
MODEL_PATH=app/models/default_model.pkl
API_KEY=your-api-key

# JWT Configuration
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=30
```

---

## Running the Service ▶️

Start the FastAPI server:

```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## API Endpoints 💽

### Health Check

```http
GET /health
```
Checks if the service is running.

---

### Sync Prediction

```http
POST /predict/{model_id}
```

**Request Body:**
```json
{
  "input": "I love this product"
}
```

**Response:**
```json
{
  "prediction": "positive sentiment"
}
```

---

### Async Prediction (Queued Processing)

```http
POST /predict-async/{model_id}
```

**Response:**
```json
{
  "task_id": "1234-abcd-5678"
}
```

Fetch result using:

```http
GET /results/{task_id}
```

---

### JIRA Integration

```http
POST /jira-predict
```

**Request Body:**
```json
{
  "query": "project = ABC AND status = 'In Testing'",
  "token": "your-jira-token"
}
```

---

## Logging & Monitoring 📊

- Logs are structured in JSON format.
- Prometheus metrics are exposed at `/metrics`.

---

## Extending the Service 🏧

### Adding New ML Models

1. Register the model in `models_config.json`:
   ```json
   {
     "models": [
       {
         "id": "new_model",
         "path": "app/models/new_model.pkl",
         "type": "sklearn"
       }
     ]
   }
   ```
2. Restart the service.

---

## Contributing 🤝

Feel free to fork and submit PRs to improve the service!

---

