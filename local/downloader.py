from django.http import HttpResponse
from django.conf import settings
from aristotle_mdr.downloader import render_to_pdf


item_register = {
    'pdf': {'comet': ['indicator']},
}


def download(request, download_type, item):
    page_size = getattr(settings, 'PDF_PAGE_SIZE', "A4")

    return render_to_pdf(
        'local/downloads/pdf/indicator.html',
        {
            'item': item,
            'subitems': [],
            'tableOfContents': False,
            'view': request.GET.get('view', '').lower(),
            'pagesize': request.GET.get('pagesize', page_size),
            'request': request,
        }
    )


def bulk_download(request, download_type, items, title=None, subtitle=None):
    res = "Not implemented yet: "
    for item in items:
        res += ', {}'.format(item)
    return HttpResponse(res, content_type="text/plain")
