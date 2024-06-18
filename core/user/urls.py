from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from core.user.views import AuthViewSet, UserPersonalityViewSet, UserAcademyGoalViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "user"
router.register("", AuthViewSet, basename="auth")
router.register("personality", UserPersonalityViewSet, basename='user_personality')
router.register("academic-goal", UserAcademyGoalViewSet, basename='user_academic_goal')

urlpatterns = router.urls
urlpatterns += [
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), 

]

