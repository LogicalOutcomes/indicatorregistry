from django.conf.urls import url, include
from django.views.generic import TemplateView
from sis_sites.ocasi.views import BrowseRegistry


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='sis_sites/ocasi/home.html'), name="ocasi_home"),
    url(r'^evaluation/$', TemplateView.as_view(template_name='sis_sites/ocasi/evaluation.html'), name="ocasi_evaluation"),
    url(r'^help/$', TemplateView.as_view(template_name='sis_sites/ocasi/help.html'), name="ocasi_help"),
    url(r'^data-portal/$', TemplateView.as_view(template_name='sis_sites/ocasi/data_portal.html'), name="ocasi_data_portal"),

    url(r'^registry/$', BrowseRegistry.as_view(), name="ocasi_registry"),
    url(r'^credits/$', TemplateView.as_view(template_name='sis_sites/ocasi/credits.html'), name="ocasi_credits"),

    url(r'^', include('logicaloutcomes.urls')),
]
