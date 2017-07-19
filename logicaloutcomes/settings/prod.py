from os.path import join
from logicaloutcomes.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['www.indicatorregistry.net', 'indicatorregistry.net', 'ocasi.indicatorregistry.net']

SIS_SITES_ROOT_URLCONF = {
    'ocasi.indicatorregistry.net': {
        'urlconf': 'sis_sites.ocasi.urls',
        'base_template': 'sis_sites/ocasi/base.html'
    }
}

SIS_SITES_DEFAULT_TEMPLATE = 'aristotle_mdr/base.html'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'indicatorregistry',
        'USER': 'user_registry',
        'PASSWORD': 'o$U0TmOl*g0N&i',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s %(levelname)s %(module)s %(process)d %(filename)s:%(lineno)d] %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s %(levelname)s] %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'applogfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(BASE_DIR, '../../logs/indicatorregistry.log'),
            'maxBytes': 1024 * 1024 * 50,  # 50MB
            'backupCount': 5,
            'formatter': 'simple',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['applogfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        '': {
            'handlers': ['applogfile'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}