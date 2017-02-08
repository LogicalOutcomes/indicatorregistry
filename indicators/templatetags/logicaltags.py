from django import template
from django.core.urlresolvers import reverse, resolve
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from aristotle_mdr import perms
import aristotle_mdr.models as MDR

register = template.Library()

@register.filter
def unique_responses(indicator):
    responses = {}
    if indicator:
        for i, d in enumerate(indicator.numerators.all()):
            for q in d.questions.all():
                for rd in q.response_domains.all():
                    vd = rd.value_domain
                    if vd:
                        _,questions = responses.get(vd.pk,(None,[]))
                        responses[vd.pk] = (vd,questions + [i])

    return responses.values()

@register.filter
def toc_slot_values(request,slot_name):
    from django.db.models import Count
    active_toc_slots = []
    for f in request.GET.getlist('sf'):
        name, value = f.split(':',1)
        if name == slot_name:
            active_toc_slots.append(value)
    from aristotle_mdr.contrib.slots.models import Slot, SlotDefinition
    slot_type_toc = SlotDefinition.objects.filter(
        app_label='comet',
        concept_type='indicator',
        slot_name=slot_name,
        cardinality = SlotDefinition.CARDINALITY.repeatable
    ).first()
    if slot_type_toc:
        slots = Slot.objects.filter(type=slot_type_toc).values('value').annotate(num=Count('concept')).distinct()
        for s in slots:
            s.update({
                'active': s['value'] in active_toc_slots,
            })
        slots = list(slots)
        slots.sort(key=lambda s:(not(s['active']),s['value'].lower()))
        return slots
    else:
        return None

@register.simple_tag
def slot_unfacet(request, field, value):
    # http://stackoverflow.com/questions/2047622/how-to-paginate-django-with-other-get-variables
    dict_ = request.GET.copy()
    if 'sf' in dict_.keys():
        f = dict_.getlist('sf')
        facet = '%s:%s' % (field, value)
        if facet in f:
            f.remove(facet)
            dict_.setlist('sf', f)

    return dict_.urlencode()

@register.simple_tag
def slot_add_facet(request, field, value):
    # http://stackoverflow.com/questions/2047622/how-to-paginate-django-with-other-get-variables
    dict_ = request.GET.copy()
    f = dict_.getlist('sf')
    
    facet = '%s:%s' % (field, value)
    if facet not in f:
        f.append(facet)
        dict_.setlist('sf', f)

    return dict_.urlencode()

@register.filter
def get_single_slot(concept, slot_name):
    if concept:
        c = concept.slots.filter(type__slot_name__iexact=slot_name).exclude(value__exact='')
        return c
    else:
        return []