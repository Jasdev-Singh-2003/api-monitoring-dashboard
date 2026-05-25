from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.decorators import throttle_classes
import time
import random

from .metrics import api_requests_total, api_errors_total, api_latency_seconds


@api_view(["GET"])
@throttle_classes([AnonRateThrottle])
def health_check(request):
    start = time.time()

    api_requests_total.labels(endpoint="health").inc()

    response = Response({"status": "healthy"}, status=200)

    api_latency_seconds.labels(endpoint="health").observe(time.time() - start)

    return response


@api_view(["GET"])
def slow_endpoint(request):
    start = time.time()

    api_requests_total.labels(endpoint="slow").inc()

    time.sleep(5)

    response = Response({"status": "slow success"}, status=200)

    api_latency_seconds.labels(endpoint="slow").observe(time.time() - start)

    return response


@api_view(["GET"])
def error_endpoint(request):
    start = time.time()

    api_requests_total.labels(endpoint="error").inc()
    api_errors_total.labels(endpoint="error").inc()

    response = Response({"status": "intentional error"}, status=500)

    api_latency_seconds.labels(endpoint="error").observe(time.time() - start)

    return response


@api_view(["GET"])
def random_status(request):
    start = time.time()

    api_requests_total.labels(endpoint="random").inc()

    code = random.choice([200, 400, 500])

    if code >= 400:
        api_errors_total.labels(endpoint="random").inc()

    response = Response({"status_code": code}, status=code)

    api_latency_seconds.labels(endpoint="random").observe(time.time() - start)

    return response
