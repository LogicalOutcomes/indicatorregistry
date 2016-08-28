from django.shortcuts import render
from comet import models
from .forms import CompareIndicatorsForm


def home(request, path=''):
    indicators = models.Indicator.objects.all() #visible(request.user)
    frameworks = models.Framework.objects.all() #visible(request.user)
    outcome_areas = models.OutcomeArea.objects.all() #visible(request.user)
    return render(request, 'aristotle_mdr/static/home.html',{
        'indicators':indicators,
        'frameworks':frameworks,
        'outcome_areas':outcome_areas,
    })


def comparer(request):
    i1 = request.GET.get('indicator_1')
    i2 = request.GET.get('indicator_2')
    i3 = request.GET.get('indicator_3')
    indicator1 = models.Indicator.objects.filter(id=i1).first() #visible(request.user)
    indicator2 = models.Indicator.objects.filter(id=i2).first() #visible(request.user)
    indicator3 = models.Indicator.objects.filter(id=i3).first() #visible(request.user)
    indicators = [indicator1,indicator2,indicator3]
    form = CompareIndicatorsForm(data=request.GET, user=request.user)
    return render(request, 'logicaloutcomes/comparer.html',{
        'indicators':indicators, "form": form
    })
