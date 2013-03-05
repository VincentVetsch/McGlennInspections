"""
WSGI config for McGlennInspections project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
# TODO -- Setup for MCGLENNINSPECTIONS
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "McGlennInspections.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
