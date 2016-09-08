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