from logicaloutcomes.settings.common import *

# Django debug toolbar
INSTALLED_APPS += ('debug_toolbar', )
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
INTERNAL_IPS = '127.0.0.1'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'indicatorregistry',
        'USER': 'user_registry',
        'PASSWORD': 'indicatorregistry',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SIS_SITES_ROOT_URLCONF = {
    'ocasi.devindicatorregistry.net:8000': {
        'urlconf': 'sis_sites.ocasi.urls',
        'base_template': 'sis_sites/ocasi/base.html'
    }
}

SIS_SITES_DEFAULT_TEMPLATE = 'sis_sites/aristotle_base.html'
