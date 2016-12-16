from logicaloutcomes.settings.common import *

# Django debug toolbar
INSTALLED_APPS += ('debug_toolbar', )
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
INTERNAL_IPS = '127.0.0.1'

DEBUG = True
