from django.conf.urls import url, include


urlpatterns = [
    # OCASI urls
    url(r'^', include('sis_sites.ocasi.urls')),
]
