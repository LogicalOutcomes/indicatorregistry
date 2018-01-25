from django.views.generic.base import RedirectView
from indicators.views import BrowseIndicatorsAsHome


class BrowseRegistry(BrowseIndicatorsAsHome):
    template_name = 'sis_sites/ocasi/registry.html'

    def get_template_names(self):
        return [self.template_name]


class MyWorkspaceView(RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        return 'https://reports.ocasi.sis.ngo'
