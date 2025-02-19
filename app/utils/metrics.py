from prometheus_client import Counter, Histogram

# Metrics for Sync Prediction
PREDICTION_HIT_COUNTER = Counter(
    "prediction_endpoint_hits", "Number of hits to the prediction endpoint"
)
PREDICTION_RESPONSE_TIME = Histogram(
    "prediction_response_time_seconds", "Response time for predictions"
)

# Metrics for Async Prediction
ASYNC_PREDICTION_HIT_COUNTER = Counter(
    "async_prediction_endpoint_hits", "Number of hits to the async prediction endpoint"
)
ASYNC_PREDICTION_RESPONSE_TIME = Histogram(
    "async_prediction_response_time_seconds", "Response time for async predictions"
)
