import base64
import os

from django.http import HttpResponse
from django_prometheus import exports


def protected_metrics(request):
    auth = request.META.get("HTTP_AUTHORIZATION")

    if not auth:
        response = HttpResponse(status=401)
        response["WWW-Authenticate"] = 'Basic realm="Metrics"'
        return response

    try:
        auth_type, credentials = auth.split()

        if auth_type.lower() != "basic":
            return HttpResponse(status=401)

        decoded = base64.b64decode(credentials).decode("utf-8")

        username, password = decoded.split(":")

        expected_user = os.getenv("METRICS_USER")
        expected_pass = os.getenv("METRICS_PASS")

        if username != expected_user or password != expected_pass:
            return HttpResponse("Invalid username/password.", status=403)

    except Exception:
        return HttpResponse(status=401)

    return exports.ExportToDjangoView(request)
