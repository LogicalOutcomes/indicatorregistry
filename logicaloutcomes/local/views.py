from django.shortcuts import render
from comet import models

def home(request, path=''):
    indicators = models.Indicator.objects.all() #visible(request.user)
    frameworks = models.Framework.objects.all() #visible(request.user)
    outcome_areas = models.OutcomeArea.objects.all() #visible(request.user)
    return render(request, 'aristotle_mdr/static/home.html',{
        'indicators':indicators,
        'frameworks':frameworks,
        'outcome_areas':outcome_areas,
    })
