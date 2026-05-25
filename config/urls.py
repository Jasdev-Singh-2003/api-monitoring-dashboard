from django.contrib import admin
from django.urls import path, include, re_path
from django_prometheus import exports
from monitoring.metrics_auth import protected_metrics

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("django_prometheus.urls")),
    path("api/", include("monitoring.urls")),
    re_path(r"^metrics$", protected_metrics),
]
