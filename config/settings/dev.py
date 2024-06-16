from .base import *

SECRET_KEY = env.str("SECRET_KEY", "*****")  


THIRD_PARTY_APPS = [
    #"rest_framework",
    #"rest_framework.authtoken",
    #"rest_framework_simplejwt.token_blacklist",
    "drf_standardized_errors",
    #"corsheaders",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    'allauth.socialaccount.providers.google',  
    "dj_rest_auth",
    "dj_rest_auth.registration",
]


LOCAL_APPS = [
    "core.accounts",
]

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
}

# SIMPLE_JWT_SETTINGS
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "AUTH_HEADER_TYPES": ("Token",),
}


# SOCIAL_LOGIN_SETTINGS
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": env.str('CLIENT_ID',"********"),  
            "secret": env.str('CLIENT_SECRET',"*******"),                                     
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "VERIFIED_EMAIL": True,
    },
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


#AUTH_USER_MODEL = 'accounts.CustomUser'