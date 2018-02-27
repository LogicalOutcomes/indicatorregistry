from os.path import join
from logicaloutcomes.settings.common import *

DEBUG = False

ALLOWED_HOSTS = [
    'indicatorregistry.net',
    'www.indicatorregistry.net',
    'ocasi.indicatorregistry.net',
    'ocasi.sis.ngo',
]

SIS_SITES_ROOT_URLCONF = {
    'ocasi.indicatorregistry.net': {
        'urlconf': 'sis_sites.ocasi.urls',
        'base_template': 'sis_sites/ocasi/base.html'
    },
    'ocasi.sis.ngo': {
        'urlconf': 'sis_sites.ocasi.urls',
        'base_template': 'sis_sites/ocasi/base.html'
    },
}

SIS_SITES_DEFAULT_TEMPLATE = 'sis_sites/aristotle_base.html'

# DATABASES = {} -- Please see local.py file for sensitive DB configuration 
# (imported by common.py, not versioned)

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
            'level': 'INFO',
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
