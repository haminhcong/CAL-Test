import os
import sys

# PATH vars

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root = lambda *x: os.path.join(BASE_DIR, *x)

# sys.path.insert(0, root('apps'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'VERY_SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
IN_TESTING = sys.argv[1:2] == ['test']

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'rolepermissions',
    # The general purpose templates
    # Optional: Skin for the admin interface
    # 'django_adminlte_theme',
    # Any apps which need to have their templates overridden by adminlte
    # 'django.contrib.admin',
]

PROJECT_APPS = [
    # 'mcos.apps.user_dashboard',
    # 'mcos.apps.lookup',
]

INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mcos.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mcos.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mcos',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

# Internationalization

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'


# Additional locations of static files

STATICFILES_DIRS = (
    root('assets'),
)
# print (root('assets'))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            root('templates'),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    }
]

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

FINGER_TABLE_SIZE = 4
RING_SIZE = 2 ** FINGER_TABLE_SIZE
REPLICA_NUM = 3

# .local.py overrides all the common settings.
try:
    from .local import *  # noqa
except ImportError:
    pass


# importing test settings file if necessary
if IN_TESTING:
    from .testing import *  # noqa
