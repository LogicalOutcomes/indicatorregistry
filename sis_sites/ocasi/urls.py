from django.conf.urls import url, include
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^', TemplateView.as_view(template_name='sis_sites/ocasi/home.html'), name="ocasi_home"),
    url(r'^evaluation/$', TemplateView.as_view(template_name='sis_sites/ocasi/evaluation.html'), name="ocasi_evaluation"),
    url(r'^credits/$', TemplateView.as_view(template_name='sis_sites/ocasi/credits.html'), name="ocasi_credits"),

    url(r'^', include('logicaloutcomes.urls')),
]
