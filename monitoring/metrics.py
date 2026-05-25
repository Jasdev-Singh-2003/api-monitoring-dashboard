from prometheus_client import Counter, Histogram

api_requests_total = Counter(
    "custom_api_requests_total", "Total API requests", ["endpoint"]
)

api_errors_total = Counter("custom_api_errors_total", "Total API errors", ["endpoint"])

api_latency_seconds = Histogram(
    "custom_api_latency_seconds", "API latency", ["endpoint"]
)
