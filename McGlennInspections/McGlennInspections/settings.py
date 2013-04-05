'''
    Django settings for McGlennInspections project.

    For more information on this file, see
    https://docs.djangoproject.com/en/dev/topics/settings/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/dev/ref/settings/
'''

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
INTERNAL_IPS = ('127.0.0.1',)

# Site Name, author, and email  -- Not standard configuration
SITENAME = "McGlenn Home Inspections"
AUTHOR = "Vincent Vetsch"
EMAIL = "vincent.vetsch@gmail.com"

AUTH_PROFILE_MODULE = 'appointment.CustomerName'
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
    'tinymce',
    'taggit',
    'blog',
    'appointment',
    'glossary',
    'rvalues',
    'slideshow',
    'navigation',
    'inspector',
    'pages',
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

'''
    Database
    https://docs.djangoproject.com/en/dev/ref/settings/#databases
'''
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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:8080',
    }
}
'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'mcglenn_cache',
    }
}

    Internationalization
    https://docs.djangoproject.com/en/dev/topics/i18n/
'''

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

'''
    Static and Media files (CSS, JavaScript, Images)
    https://docs.djangoproject.com/en/dev/howto/static-files/
'''
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)
MEDIA_ROOT = '/home/vince/Projects/McInspWork/sites/www.McGlennInspections.com/htdocs/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/vince/Projects/McInspWork/sites/www.McGlennInspections.com/htdocs/static/'
STATIC_URL = '/static/'

'''
    Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    Always use forward slashes, even on Windows.
    Don't forget to use absolute paths, not relative paths.
'''
TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                                "django.core.context_processors.debug",
                                "django.core.context_processors.i18n",
                                "django.core.context_processors.media",
                                "django.core.context_processors.static",
                                "django.core.context_processors.tz",
                                "django.contrib.messages.context_processors.messages",
                                "django.core.context_processors.request",
)
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
    'theme': "advanced",
    'theme_advanced_toolbar_location': "top",
    'width': '700',
    'height': '400',
    'theme_advanced_buttons1': "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,fontselect,fontsizeselect,fullscreen,code",
    'theme_advanced_buttons2': "bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,|,forecolor,backcolor",
    'theme_advanced_buttons3': "tablecontrols,|,hr,sub,sup,|,charmap",
    'theme_advanced_resizing': "true",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TEMPLATE_DIRS = (
    'templates',
    'blog/templates',
    'application/templates',
    'glossary/templates',
    'rvalues/templates',
    'slideshow/templates',
    'cust_feedback/templates',
    'navigation/templates',
    'inspector/templates',
    'pages/templates',
)
#ADMIN_MEDIA_PREFIX = '/static/admin'
