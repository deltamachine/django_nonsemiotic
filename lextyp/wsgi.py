"""
WSGI config for lextyp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lextyp.settings")

import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

application = get_wsgi_application()
