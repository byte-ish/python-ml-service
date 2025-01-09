# Monitoring and Metrics

This guide provides detailed instructions on how monitoring and metrics are implemented in the ML microservice, leveraging Prometheus and its ecosystem. It includes how to set up, monitor, and expand metrics collection to maintain and observe the microservice's health, performance, and usage.

---

## Table of Contents

1. [Overview](#overview)
2. [Prometheus Metrics Integration](#prometheus-metrics-integration)
3. [Implemented Metrics](#implemented-metrics)
    - [Prediction Endpoint Hit Counter](#prediction-endpoint-hit-counter)
    - [Prediction Response Time Histogram](#prediction-response-time-histogram)
4. [Exposing Metrics Endpoint](#exposing-metrics-endpoint)
5. [Monitoring Setup](#monitoring-setup)
    - [Installing Prometheus](#installing-prometheus)
    - [Configuring Prometheus](#configuring-prometheus)
    - [Visualizing with Grafana](#visualizing-with-grafana)
6. [Extending Metrics](#extending-metrics)
7. [Best Practices](#best-practices)

---

## Overview

Monitoring and metrics are critical components for ensuring the reliability and performance of the microservice. By leveraging Prometheus, the microservice can collect, store, and analyze various metrics in real-time. Metrics such as endpoint hit counts and response times provide insights into the system's health, usage patterns, and potential bottlenecks.

---

## Prometheus Metrics Integration

Prometheus metrics are seamlessly integrated into the FastAPI application using the `prometheus-fastapi-instrumentator` library. This library instruments the application to collect metrics without additional boilerplate code.

Key integration points:
1. **Instrumentation during application initialization**:
    - Metrics collection is configured in `main.py`.
    - All metrics are exposed via the `/metrics` endpoint for Prometheus scraping.

```python
from prometheus_fastapi_instrumentator import Instrumentator

# Configure Prometheus Instrumentation
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)
```

2. **Custom Metrics**:
    - Custom metrics, such as endpoint-specific counters and histograms, are defined in `utils/metrics.py`.

---

## Implemented Metrics

### Prediction Endpoint Hit Counter

**Metric Name**: `prediction_endpoint_hits`

- **Description**: Tracks the number of hits to the prediction endpoint.
- **Type**: Counter
- **Purpose**: Monitors the frequency of prediction requests, useful for understanding usage patterns.

Implementation:
```python
from prometheus_client import Counter

PREDICTION_HIT_COUNTER = Counter(
    "prediction_endpoint_hits",
    "Number of hits to the prediction endpoint"
)
```

Usage:
```python
PREDICTION_HIT_COUNTER.inc()  # Increment the counter
```

---

### Prediction Response Time Histogram

**Metric Name**: `prediction_response_time_seconds`

- **Description**: Captures the distribution of response times for predictions.
- **Type**: Histogram
- **Purpose**: Helps identify latency issues and optimize performance.

Implementation:
```python
from prometheus_client import Histogram

PREDICTION_RESPONSE_TIME = Histogram(
    "prediction_response_time_seconds",
    "Response time for predictions",
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
)
```

Usage:
```python
with PREDICTION_RESPONSE_TIME.time():
    # Code block to measure response time
```

---

## Exposing Metrics Endpoint

The `/metrics` endpoint is automatically exposed by the `prometheus-fastapi-instrumentator` library, making it accessible for Prometheus to scrape. To access it, visit:

```
http://<host>:<port>/metrics
```

Sample output:
```
# HELP prediction_endpoint_hits Number of hits to the prediction endpoint
# TYPE prediction_endpoint_hits counter
prediction_endpoint_hits 42
```

---

## Monitoring Setup

### Installing Prometheus

1. Download Prometheus from its [official website](https://prometheus.io/download/).
2. Extract the package and navigate to the directory.
3. Start Prometheus using:
   ```bash
   ./prometheus --config.file=prometheus.yml
   ```

### Configuring Prometheus

1. Open the `prometheus.yml` file and add a job to scrape metrics from the microservice:
   ```yaml
   scrape_configs:
     - job_name: 'ml_microservice'
       static_configs:
         - targets: ['localhost:8000']  # Replace with your host and port
   ```

2. Restart Prometheus to apply the configuration.

### Visualizing with Grafana

1. Install Grafana by following the [official guide](https://grafana.com/grafana/download).
2. Add Prometheus as a data source in Grafana.
3. Create custom dashboards to visualize metrics such as hit counts and response times.

---

## Extending Metrics

To add new custom metrics:
1. Define the metric in `utils/metrics.py` using Prometheus client types (e.g., Counter, Histogram).
2. Increment or observe the metric in the relevant service or route.
3. Expose the metric through the `/metrics` endpoint.

Example:
```python
from prometheus_client import Summary

NEW_METRIC = Summary("new_metric", "Description of the new metric")

# Usage
NEW_METRIC.observe(value)
```

---

## Best Practices

1. **Start with key metrics**:
   - Focus on request counts, latencies, and error rates as a foundation.

2. **Keep metrics meaningful**:
   - Avoid overloading the system with redundant or unnecessary metrics.

3. **Use labels effectively**:
   - Add labels (e.g., `endpoint`, `status_code`) to metrics for better filtering and analysis.

4. **Monitor resource usage**:
   - Include metrics for CPU and memory utilization to ensure system health.

5. **Leverage Grafana**:
   - Use Grafana dashboards for a more user-friendly visualization of your Prometheus data.

---

With these monitoring and metrics practices, your ML microservice will be well-equipped for observability, ensuring optimal performance and reliability.