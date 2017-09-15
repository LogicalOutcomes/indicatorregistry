from logicaloutcomes.settings.common import *

CELERY_TASK_ALWAYS_EAGER = True

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

STATIC_ROOT = BASE_DIR + 'static/'