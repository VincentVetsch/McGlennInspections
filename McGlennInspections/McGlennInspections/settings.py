"""
    Django settings for McGlennInspections project.

    For more information on this file, see
    https://docs.djangoproject.com/en/dev/topics/settings/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

'''
    Quick-start development settings - unsuitable for production

    SECURITY WARNING: keep the secret key used in production secret!
    Hardcoded values can leak through source control. Consider loading
    the secret key from an environment variable or a file instead.
'''
SECRET_KEY = 'hbs*t#g76q7un&=w8734v4c3=4+0dko_#_7i*o5a5=fxcn0(%a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (
    'templates',
    'blog/templates',
    'application/templates',
    'glossary/templates',
    'rvalues/templates',
    'slideshow/templates',
)
INTERNAL_IPS = ('127.0.0.1',)

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django_extensions',
    'taggit',
    'blog',
    'appointment',
    'glossary',
    'rvalues',
    'slideshow',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'McGlennInspections.urls'

WSGI_APPLICATION = 'McGlennInspections.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# TODO - Change password for production server

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mcglenn',
        'USER': 'mcglenn',
        'PASSWORD': 'BG5CpLGEntWnAhxe',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = '/static/'
