from aristotle_mdr.downloader import render_to_pdf, items_for_bulk_download
from django.conf import settings
from django.utils.safestring import mark_safe


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
    """Built in download method"""
    template = 'local/downloads/pdf/bulk_download.html'  # %(download_type)
    page_size = getattr(settings, 'PDF_PAGE_SIZE', "A4")

    item_querysets = items_for_bulk_download(items, request)

    if title is None:
        if request.GET.get('title', None):
            title = request.GET.get('title')
        else:
            title = "Auto-generated document"

    if subtitle is None:
        if request.GET.get('subtitle', None):
            subtitle = request.GET.get('subtitle')
        else:
            _list = "<li>" + "</li><li>".join([item.name for item in items if item]) + "</li>"
            subtitle = mark_safe("Generated from the following metadata items:<ul>%s<ul>" % _list)

    if download_type == "pdf":
        debug_as_html = bool(request.GET.get('html', ''))

        return render_to_pdf(
            template,
            {
                'title': title,
                'subtitle': subtitle,
                'items': items,
                'included_items': sorted(
                    [(k, v) for k, v in item_querysets.items()],
                    key=lambda k_v: k_v[0]._meta.model_name
                ),
                'pagesize': request.GET.get('pagesize', page_size),
            },
            debug_as_html=debug_as_html
        )
