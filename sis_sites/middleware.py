from django.shortcuts import redirect


class SISSitesMiddleware(object):
    def process_request(self, request):
        import ipdb; ipdb.set_trace()
        return None