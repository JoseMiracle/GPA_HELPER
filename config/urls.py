"""
URL configuration for gpahelper project.

"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"api/v{settings.API_VERSION}/accounts/", include('core.accounts.api.urls'), name='accounts'),
]
