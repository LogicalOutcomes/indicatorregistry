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
#from aristotle_cloud.settings import *
from aristotle_mdr.required_settings import *

# Override these
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.join(BASE_DIR, 'site')
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
FIXTURES_DIRS = [os.path.join(BASE_DIR, 'fixtures')]
STATIC_ROOT =os.path.join(BASE_DIR, "static")

# If you are using the Aristotle Glossary, uncomment the command below to enable
# the glossary insertion button in the rich text editor
#from aristotle_glossary.settings import CKEDITOR_CONFIGS

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
     'logicaloutcomes',
     'comet',
     'mallard_qr',
     'aristotle_ddi_utils', # Download formats in the DDI3.2 XML format - https://github.com/aristotle-mdr/aristotle-ddi-utils
     #'aristotle_dse', # Additional models for describing datasets - https://github.com/aristotle-mdr/aristotle-dataset-extensions
     #'aristotle_glossary', # Model for managing and inserting glossary content - https://github.com/aristotle-mdr/aristotle-glossary
     #'aristotle_mdr_api', # JSON API for programmatic access to content
     #'rest_framework', # Needed for the above
) + INSTALLED_APPS # Installs the required apps to run aristotle.

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

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#Aristotle settings are below, settings these gives the ability to personalise this particular installation.
ARISTOTLE_SETTINGS.update({
    'SITE_NAME': 'Logical Outcomes Indicator Register', # 'The main title for the site.'
    'SITE_BRAND': '/static/aristotle_mdr/images/aristotle_small.png', # URL for the Site-wide logo
    'SITE_INTRO': 'Search for financial literacy indicators below...', # 'Intro text use on the home page as a prompt for users.'
    'SITE_DESCRIPTION': 'About this site', # 'The main title for the site.'
    'CONTENT_EXTENSIONS' : [ #Extensions that add additional object types for search/display.
             'aristotle_dse',
             'aristotle_glossary',
             'comet',
             'mallard_qr',
             'logicaloutcomes',
        ],
    'BULK_ACTIONS': {
        'add_favourites': 'aristotle_mdr.forms.bulk_actions.AddFavouriteForm',
        'remove_favourites': 'aristotle_mdr.forms.bulk_actions.RemoveFavouriteForm',
        'change_state': 'aristotle_mdr.forms.bulk_actions.ChangeStateForm',
        'move_workgroup': 'aristotle_mdr.forms.bulk_actions.ChangeWorkgroupForm',
        'request_review': 'aristotle_mdr.forms.bulk_actions.RequestReviewForm',
        #'bulk_download': 'aristotle_mdr.forms.bulk_actions.BulkDownloadForm',
        'export': 'logicaloutcomes.local.forms.QuickPDFExportDownloadForm',
        'compare': 'logicaloutcomes.local.forms.CompareRedirectBulkActionForm',
    },
    })
# Specified the agency to use when outputing items in the DDI XML format.
ARISTOTLE_DDI_AGENCY = "demo.ddi.aristotle_mdr"

# This option gives a site the ability to register the different download options available for the site
# This invoked in templates using the aristotle template tag "downloadMenu"
ARISTOTLE_DOWNLOADS = [
    ('pdf', 'PDF', 'fa-file-pdf-o', 'aristotle_mdr', 'Downloads for various content types in the PDF format'),
    ]


#from aristotle_cloud import plans
#MODEL_LIMITS = plans.PLANS['large']

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        'INCLUDE_SPELLING':True,
    },
}