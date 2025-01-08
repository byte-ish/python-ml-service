"""
Prometheus Metrics for Monitoring the ML Microservice.
"""

from prometheus_client import Counter, Histogram

# Counter to track the number of hits to the prediction endpoint
PREDICTION_HIT_COUNTER = Counter(
    "prediction_endpoint_hits",
    "Number of hits to the prediction endpoint"
)

# Histogram to track the response time for predictions
# Buckets are configured to provide meaningful latency distribution data
PREDICTION_RESPONSE_TIME = Histogram(
    "prediction_response_time_seconds",
    "Response time for predictions",
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
)
