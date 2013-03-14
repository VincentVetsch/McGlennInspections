'''
    WSGI config for McGlennInspections project.

    It exposes the WSGI callable as a module-level variable named ``application``.

    For more information on this file, see
    https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
'''

import os
import os.path
import sys

sys.path.append('/home/vince/Projects/McInspWork/McGlennInspections/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "McGlennInspections.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
