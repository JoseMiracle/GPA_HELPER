import re

from django.conf import settings

from django.http import HttpResponse
from rest_framework import viewsets, decorators, status, response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from drf_spectacular.utils import extend_schema

from core.user.models import User
from core.user import serializers
from core.utils.mixins import CustomRequestDataValidationMixin, CountListResponseMixin
from core.user.models import UserSession
from core.utils import permissions, exceptions, google_oauth


"""def receive_auth_test(request):
    print(request.data)
    return HttpResponse({"status": 'success'})"""


class AuthViewSet(
    CustomRequestDataValidationMixin, CountListResponseMixin, viewsets.ViewSet
):
    queryset = User.objects
    #http_method_names = ["post", "get"]
    serializer_class = serializers.Retrieve

    def get_queryset(self):
        return self.queryset.all()

    def get_required_fields(self):
        if self.action == "google_login":
            return ["redirect_uri_content"]
        if self.action == "initialize_google_login":
            return ["redirect_uri"]

        if self.action == "school_data":
            return ["school", "faculty", "department", "level", "timetable"]

        return []

    def get_permissions(self):
        if self.action in [
            "initialize_google_login",
            "google_login",
        ]:
            return [permissions.IsGuestUser()]
        return super().get_permissions()

    @staticmethod
    def get_redirect_uri_from_redirect_uri_content(redirect_uri_content: str):
        pattern = re.compile(r"(.+)\?.+")
        match_pattern = pattern.match(redirect_uri_content)
        print(match_pattern)
        if match_pattern:
            print(match_pattern.group(1))
            return match_pattern.group(1)

    def logout(self, request, *args, **kwargs):

        try:
            UserSession.objects.get(refresh=request.data.get("token")).delete()
            refresh_token = request.data.get("token")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except TokenError as err:
            raise exceptions.CustomException(
                status_code=status.HTTP_400_BAD_REQUEST,
                message=str(err),
                errors=["refresh token error"],
            )
        except UserSession.DoesNotExist as err:
            raise exceptions.CustomException(
                status_code=status.HTTP_400_BAD_REQUEST,
                message=str(err),
                errors=["refresh token error"],
            )

    @decorators.action(
        detail=False,
        methods=["get"],
        name="me",
        url_path="me",
    )
    def me(self, request, *args, **kwargs):
        serializer = serializers.Retrieve(instance=request.user)
        return response.Response(status=status.HTTP_200_OK, data=serializer.data)

    @decorators.action(detail=False, methods=["post"])
    def initialize_google_login(self, request, *args, **kwargs):
        redirect_uri = request.data.get("redirect_uri")
        redirect_uri: str = redirect_uri.strip()

        if redirect_uri.endswith("/"):
            redirect_uri = redirect_uri.rstrip("/")

        google_oauth_helper = google_oauth.GoogleOauthHelper(redirect_uri)
        oauth_url = google_oauth_helper.get_oauth_url()
        return response.Response(
            status=status.HTTP_200_OK, data={"oauth_url": oauth_url}
        )

    @decorators.action(detail=False, methods=["post"])
    def google_login(self, request, *args, **kwargs):
        redirect_uri_content = request.data.get("redirect_uri_content")
        redirect_uri = self.get_redirect_uri_from_redirect_uri_content(
            redirect_uri_content
        )
        if not redirect_uri:
            raise exceptions.CustomException(
                errors=["invalid redirect_uri_content"],
                message="Unable to parse submitted 'redirect_uri_content'",
            )

        google_oauth_helper = google_oauth.GoogleOauthHelper(redirect_uri)
        try:
            user_profile, credentials = google_oauth_helper.authenticate_process(
                request, redirect_uri_content
            )
        except Exception as err:
            raise exceptions.CustomException(
                message="Unable to authenticate user",
                errors="Unable to authenticate user",
            )
        else:
            email = user_profile["email"].lower()
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                setattr(
                    user,
                    "google_auth_credentials",
                    credentials,
                )
                user.save()
            else:
                user_data = {
                    "email": email,
                    "first_name": user_profile.get("given_name"),
                    "google_auth_credentials": credentials,
                }
                user = User.objects.create(**user_data)
                user.set_password(settings.SECRET_KEY)

            auth_token = user.retrieve_auth_token()
            session = UserSession.objects.filter(user=user).first()

            if session and session.is_active:
                try:
                    token = RefreshToken(session.refresh)
                    token.blacklist()
                except Exception as e:
                    raise exceptions.CustomException(
                        message="unable to blacklist token"
                    )
                session.delete()
            else:
                UserSession.objects.create(
                    user=user,
                    refresh=auth_token["refresh"],
                    access=auth_token["access"],
                    ip_address=request.META.get("REMOTE_ADDR"),
                    user_agent=request.META.get("HTTP_USER_AGENT"),
                    is_active=True,
                )

            serializer = serializers.Retrieve(instance=user)
            response_data = {**serializer.data, "token": auth_token}
            return response.Response(status=status.HTTP_200_OK, data=response_data)

    @extend_schema(request=serializers.SchoolUpdate())
    @decorators.action(
        detail=False,
        methods=["patch"],
        url_path="school-details"
    )
    def school_data(self, request, *args, **kwargs):
        """
        This endpoint updates school data for a user.
        """
        
        serializer = serializers.SchoolUpdate(
            instance=request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = serializers.Retrieve(instance=request.user)
        return response.Response(status=status.HTTP_200_OK, data=serializer.data)
