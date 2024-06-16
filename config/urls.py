"""
URL configuration for gpahelper project.

"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"api/v{settings.API_VERSION}/users/", include("core.user.urls"), name="user"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
