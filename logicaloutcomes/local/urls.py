from django.conf.urls import patterns, include, url
from logicaloutcomes.local import views
from django.views.generic import TemplateView
from aristotle_mdr.contrib.browse.views import BrowseConcepts
#from comet.models import Indicator

# Below are the 'recommended' locations for the paths to aristotle extensions.
urlpatterns = [
    #url(r'^/?$', views.home, name='lo_home'),
    url(r'^/?$', views.BrowseIndicatorsAsHome.as_view(), name='lo_home'),
    # url(r'^export/?$', views.ExportIndicators.as_view(), name='exporter'),
    url(r'^export/?$', TemplateView.as_view(template_name='logicaloutcomes/static/export.html'), name="exporter"),
    url(r'^comparer/?$', views.comparer, name='comparer'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect': '/user/password/done/'},
        name='password_reset_confirm',),
    url(r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),

    url(r'^about/?$', TemplateView.as_view(template_name='logicaloutcomes/static/about.html'), name="about"),
    url(r'^contact/?$', TemplateView.as_view(template_name='logicaloutcomes/static/contact.html'), name="contact"),
    url(r'^terms_of_use/?$', TemplateView.as_view(template_name='logicaloutcomes/static/terms_of_use.html'), name="terms_of_use"),
    url(r'^privacy/?$', TemplateView.as_view(template_name='logicaloutcomes/static/privacy.html'), name="privacy"),

    ]
