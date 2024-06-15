"""
WSGI config for gpahelper project.

It exposes the WSGI callable as a module-level variable named ``application``.


"""

import os

from django.core.wsgi import get_wsgi_application
from. import env
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", env.str("DJANGO_SETTINGS_MODULE", "config.settings.prod")
)


application = get_wsgi_application()
