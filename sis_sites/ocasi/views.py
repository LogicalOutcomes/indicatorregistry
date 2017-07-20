from indicators.views import BrowseIndicatorsAsHome


class BrowseRegistry(BrowseIndicatorsAsHome):
    template_name = 'sis_sites/ocasi/registry.html'

    def get_template_names(self):
        return [self.template_name]
