# app.py
from flask import Flask, jsonify
from prometheus_client import generate_latest, Counter, Histogram
import time

app = Flask(__name__)

# Define a Counter metric
# This counter will increment every time the health endpoint is called.
HEALTH_CHECK_CALLS = Counter(
    'health_check_calls_total',
    'Total number of times the health check endpoint has been called.'
)

# Define a Histogram metric for request duration
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'Histogram of request duration in seconds.',
    ['endpoint'] # Label for the endpoint
)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    Increments the health check calls counter.
    Returns:
        JSON: {"status": "ok"} if the service is up.
    """
    start_time = time.time()
    HEALTH_CHECK_CALLS.inc() # Increment the counter
    response = jsonify({"status": "ok"})
    REQUEST_LATENCY.labels('/health').observe(time.time() - start_time) # Observe latency
    return response

@app.route('/metrics')
def metrics():
    """
    Prometheus metrics endpoint.
    Returns:
        Prometheus metrics in plaintext format.
    """
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

if __name__ == '__main__':
    # Listen on all public IPs, suitable for Docker/Kubernetes
    app.run(host='0.0.0.0', port=5000)
