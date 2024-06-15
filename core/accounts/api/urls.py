from core.accounts.api.views import GoogleLoginView
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('google-login/', GoogleLoginView.as_view(), name='google_login'),
]

