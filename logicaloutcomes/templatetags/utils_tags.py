import datetime

from django import template
from django.conf import settings
from django.core.urlresolvers import reverse, resolve
from django.utils import dateformat

register = template.Library()

@register.filter
def order_by(qs,order):
    return qs.order_by(*(order.split(",")))
