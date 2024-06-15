"""
URL configuration for gpahelper project.

"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('gpahelper.accounts.api.urls'), name='accounts'),
]
