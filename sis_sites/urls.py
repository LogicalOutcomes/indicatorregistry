from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [

    # OCASI urls
    url(r'^ocasi/$', TemplateView.as_view(template_name='sis_sites/ocasi/home.html'), name="ocasi_home"),
    url(r'^ocasi/evaluation/$', TemplateView.as_view(template_name='sis_sites/ocasi/evaluation.html'), name="ocasi_evaluation"),
    url(r'^ocasi/credits/$', TemplateView.as_view(template_name='sis_sites/ocasi/credits.html'), name="ocasi_credits"),
]
