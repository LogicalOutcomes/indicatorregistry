# from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView
from indicators.views import BrowseIndicatorsAsHome


class BrowseRegistry(BrowseIndicatorsAsHome):
    template_name = 'sis_sites/ocasi/registry.html'

    def get_template_names(self):
        return [self.template_name]


class MyWorkspaceView(TemplateView):
    template_name = 'sis_sites/ocasi/my_workspace.html'


# class MyWorkspaceView(RedirectView):

#     permanent = False
#     query_string = True

#     def get_redirect_url(self, *args, **kwargs):
#         return 'https://reports.ocasi.sis.ngo'
