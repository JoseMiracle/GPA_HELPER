from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3001/"
    client_class = OAuth2Client


    def dispatch(self, request, *args, **kwargs):
        """
           Overriding the dispatch method to customize the response:
            - Remove the temporary 'key' generated during authentication.
            - Create an access token for the authenticated user and add it to the response.
            This approach is used as we are not using Token-based authentication.
        """
        response = super().dispatch(request, *args, **kwargs) 
        try: 
            key = response.data['key']
            user_id_associated_with_token = Token.objects.filter(key=key).first().user.id
            user = User.objects.filter(id=user_id_associated_with_token).first()
            response.data.pop('key')
            response.data['access_token'] = str(RefreshToken.for_user(user).access_token)
            return response
        
        except Exception :
            return response
        
        
    
