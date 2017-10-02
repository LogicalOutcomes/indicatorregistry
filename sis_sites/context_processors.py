from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404
from django.shortcuts import get_object_or_404


def flatpages(request):
    site_id = get_current_site(request).id
    try:
        return {
            'flatpage': get_object_or_404(FlatPage, url=request.path, sites=site_id)
        }
    except Http404:
        return {}
