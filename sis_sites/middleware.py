from django.conf import settings


class SISSitesMiddleware(object):
    def process_request(self, request):
        host = request.get_host()
        if host in settings.SIS_SITES_ROOT_URLCONF:
            request.urlconf = settings.SIS_SITES_ROOT_URLCONF[host]['urlconf']
            request.base_template = settings.SIS_SITES_ROOT_URLCONF[host]['base_template']
        else:
            request.base_template = settings.SIS_SITES_DEFAULT_TEMPLATE
