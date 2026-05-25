from django.urls import path
from .views import health_check, slow_endpoint, error_endpoint, random_status

urlpatterns = [
    path("health/", health_check),
    path("slow/", slow_endpoint),
    path("error/", error_endpoint),
    path("random/", random_status),
]
