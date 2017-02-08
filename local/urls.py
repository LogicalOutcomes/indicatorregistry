from django.conf.urls import url
from django.views.generic import TemplateView


# Below are the 'recommended' locations for the paths to aristotle extensions.
urlpatterns = [
    url(r'^about/?$', TemplateView.as_view(template_name='static/about.html'), name="about"),
    url(r'^contact/?$', TemplateView.as_view(template_name='static/contact.html'), name="contact"),
    url(r'^terms_of_use/?$', TemplateView.as_view(template_name='static/terms_of_use.html'), name="terms_of_use"),
    url(r'^privacy/?$', TemplateView.as_view(template_name='static/privacy.html'), name="privacy"),
]
