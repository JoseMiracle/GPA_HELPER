"""
ASGI config for gpahelper project.

It exposes the ASGI callable as a module-level variable named ``application``.

"""

import os

from django.core.asgi import get_asgi_application
from . import env

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", env.str("DJANGO_SETTINGS_MODULE", "config.settings.prod")
)

app = get_asgi_application()
