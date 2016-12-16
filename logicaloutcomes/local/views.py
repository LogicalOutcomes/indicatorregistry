from aristotle_mdr.contrib.browse.views import BrowseConcepts
from comet import models
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .forms import CompareIndicatorsForm


class BrowseIndicatorsAsHome(BrowseConcepts):
    _model = models.Indicator
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        self.kwargs['app'] = 'comet'
        context = super(BrowseIndicatorsAsHome, self).get_context_data(**kwargs)
        return context


class ExportIndicators(BrowseConcepts):
    _model = models.Indicator
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        self.kwargs['app'] = 'comet'
        context = super(ExportIndicators, self).get_context_data(**kwargs)
        return context

    def get_template_names(self):
        return "logicaloutcomes/export_indicators.html"


# def home(request, path=''):
#     indicators = models.Indicator.objects.all() #visible(request.user)
#     frameworks = models.Framework.objects.all() #visible(request.user)
#     outcome_areas = models.OutcomeArea.objects.all() #visible(request.user)
#     return render(request, 'aristotle_mdr/static/home.html',{
#         'indicators':indicators,
#         'frameworks':frameworks,
#         'outcome_areas':outcome_areas,
#     })


def comparer(request):
    if request.GET.getlist('items', None):
        i1, i2, i3 = (request.GET.getlist('items')+[None,None,None])[:3]
        data = {
            'indicator_1': i1,
            'indicator_2': i2,
            'indicator_3': i3,
        }
    else:
        i1 = request.GET.get('indicator_1', None)
        i2 = request.GET.get('indicator_2', None)
        i3 = request.GET.get('indicator_3', None)
        data = request.GET
    indicator1 = models.Indicator.objects.filter(id=i1).first() #visible(request.user)
    indicator2 = models.Indicator.objects.filter(id=i2).first() #visible(request.user)
    indicator3 = models.Indicator.objects.filter(id=i3).first() #visible(request.user)
    indicators = [indicator1,indicator2,indicator3]
    form = CompareIndicatorsForm(data=data, user=request.user)
    return render(request, 'logicaloutcomes/comparer.html',{
        'indicators':indicators, "form": form
    })


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def handler403(request):
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response


def handler400(request):
    response = render_to_response('400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response
