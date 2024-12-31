from prometheus_client import Counter, Histogram

# Custom Prometheus Metrics
PREDICTION_HIT_COUNTER = Counter(
    "prediction_endpoint_hits", "Number of hits to the prediction endpoint"
)
PREDICTION_RESPONSE_TIME = Histogram(
    "prediction_response_time_seconds", "Response time for predictions"
)