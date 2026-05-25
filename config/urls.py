from django.contrib import admin
from django.urls import path, include, re_path
from basicauth.decorators import basic_auth_required
from django_prometheus import exports

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("django_prometheus.urls")),
    path("api/", include("monitoring.urls")),
    re_path(
        r"^metrics$",
        basic_auth_required(exports.ExportToDjangoView),
    ),
]
