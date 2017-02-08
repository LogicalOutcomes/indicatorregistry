from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from aristotle_mdr.contrib.browse.views import BrowseConcepts
from .views import BrowseIndicatorsAsHome, comparer

# Below are the 'recommended' locations for the paths to aristotle extensions.
urlpatterns = [
    #url(r'^/?$', views.home, name='lo_home'),
    url(r'^/?$', BrowseIndicatorsAsHome.as_view(), name='lo_home'),
    # url(r'^export/?$', views.ExportIndicators.as_view(), name='exporter'),
    url(r'^export/?$', TemplateView.as_view(template_name='indicators/static/export.html'), name="exporter"),
    url(r'^comparer/?$', comparer, name='comparer'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect': '/user/password/done/'},
        name='password_reset_confirm',),
    url(r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),
]
