"""
Django settings for logicaloutcomes project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/

# Quick-start development settings - unsuitable for production
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Import all of the necessary settings to get the Aristotle server working.
# These are defaults and can be overridden within this file.
from aristotle_mdr.required_settings import *

# Override these
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.join(BASE_DIR, 'site')
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
FIXTURES_DIRS = [os.path.join(BASE_DIR, 'fixtures')]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# If you are using the Aristotle Glossary, uncomment the command below to enable
# the glossary insertion button in the rich text editor
# from aristotle_glossary.settings import CKEDITOR_CONFIGS

# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# You need to
SECRET_KEY = '0304c93f04cfb9cdfd26f8d82a68ff944dc3f2f3a6abd547ce496413'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition
# Below is a barebones "INSTALLED_APPS" configuration for Aristotle.
# Some extra apps are included, but commented out, to demonstrate how to add additional apps.
# To install these uncomment the lines for the apps you want in the following locations:
# * INSTALLED_APPS setting in this file (just below)
# * CONTENT_EXTENSIONS setting in this file in ARISTOTLE_SETTINGS
# * the installation command in `requirements.txt` file
# * the url import in `logicaloutcomes/urls.py`
INSTALLED_APPS = (
    'sis_sites',
    'aristotle_themes',
    'local',
    'indicators',
    'comet',
    'mallard_qr',
    'django_celery_results',
    # Static pages
    'django.contrib.sites',
    'django.contrib.flatpages',
    'pagedown',
    'markdown_deux',
    # 'aristotle_ddi_utils', # Download formats in the DDI3.2 XML format - https://github.com/aristotle-mdr/aristotle-ddi-utils
    #'aristotle_dse', # Additional models for describing datasets - https://github.com/aristotle-mdr/aristotle-dataset-extensions
    #'aristotle_glossary', # Model for managing and inserting glossary content - https://github.com/aristotle-mdr/aristotle-glossary
    #'aristotle_mdr_api', # JSON API for programmatic access to content
    #'rest_framework', # Needed for the above
) + INSTALLED_APPS # Installs the required apps to run aristotle.

# Use domain to detect site
SITE_ID = None

ROOT_URLCONF = 'logicaloutcomes.urls'


WSGI_APPLICATION = 'logicaloutcomes.wsgi.application'


# Database
# Below is the default database setup, which uses the file-based SQLite database.
# For production systems, examine the django guide below to getting other databases configured.
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'aristotle_mdr.contrib.redirect.middleware.RedirectMiddleware',
    'sis_sites.middleware.SISSitesMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#Aristotle settings are below, settings these gives the ability to personalise this particular installation.
ARISTOTLE_SETTINGS.update({
    'SITE_NAME': 'LogicalOutcomes Indicator Registry', # 'The main title for the site.'
    'SITE_BRAND': '/static/img/logicaloutcomes.png', # URL for the Site-wide logo
    'SITE_INTRO': 'Search for financial literacy indicators below...', # 'Intro text use on the home page as a prompt for users.'
    'SITE_DESCRIPTION': 'About this site', # 'The main title for the site.'
    'SITE_FAVICON': 'http://logicaloutcomes.net/wp-content/uploads/2015/09/cropped-LO-icon-only-32x32.jpg',
    'THEMES_MAIN_SCSS': 'scss/indicatorregistry_theme.scss',
    'THEMES_NAME': '',
    'DASHBOARD_ADDONS': ['indicators'],
    'CONTENT_EXTENSIONS' : [ #Extensions that add additional object types for search/display.
             'aristotle_dse',
             'aristotle_glossary',
             'comet',
             'mallard_qr',
             'indicators',
        ],
    'BULK_ACTIONS': {
        'add_favourites': 'aristotle_mdr.forms.bulk_actions.AddFavouriteForm',
        'remove_favourites': 'aristotle_mdr.forms.bulk_actions.RemoveFavouriteForm',
        'change_state': 'aristotle_mdr.forms.bulk_actions.ChangeStateForm',
        'move_workgroup': 'aristotle_mdr.forms.bulk_actions.ChangeWorkgroupForm',
        'request_review': 'aristotle_mdr.forms.bulk_actions.RequestReviewForm',
        'bulk_download': 'aristotle_mdr.forms.bulk_actions.BulkDownloadForm',
        # 'export': 'indicators.forms.QuickPDFExportDownloadForm',
        'compare': 'indicators.forms.CompareRedirectBulkActionForm',
    },
})

# Specified the agency to use when outputing items in the DDI XML format.
ARISTOTLE_DDI_AGENCY = "demo.ddi.aristotle_mdr"

# This option gives a site the ability to register the different download options available for the site
# This invoked in templates using the aristotle template tag "downloadMenu"
ARISTOTLE_DOWNLOADS = [
    ('pdf', 'PDF', 'fa-file-pdf-o', 'aristotle_mdr', 'Downloads for various content types in the PDF format'),
    ('pdf', 'PDF Summary', 'fa-file-pdf-o', 'local', 'Downloads indicators in simple PDF format'),
    ('dhis2', 'DHIS2', 'fa-cloud-upload', 'indicators', 'Export to DHIS2 using API'),
]


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        'INCLUDE_SPELLING': True,
    },
}

STATIC_PRECOMPILER_COMPILERS = (
    ('static_precompiler.compilers.LESS', {"executable": "lesscpy"}),
    ('static_precompiler.compilers.libsass.SCSS', {
        "sourcemap_enabled": True,
        "precision": 8,
    })
)

CELERY_RESULT_BACKEND = 'django-db'

# import local.py file if possible to overwrite local configuration like secret keys
try:
    from .local import *
except ImportError:
    pass

