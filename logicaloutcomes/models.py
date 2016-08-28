from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from model_utils import Choices

from aristotle_mdr.models import RichTextField
import aristotle_mdr as aristotle
from comet.models import Indicator


class Population(models.Model):
    object_class = models.ForeignKey(
        aristotle.models.ObjectClass,
    )
    indicator = models.ForeignKey(
        Indicator,
        related_name='populations'
    )

class Instrument(aristotle.models.concept):
    template = "logicaloutcomes/instrument.html"
    # population = models.ForeignKey(Population, null=True)
    population = aristotle.models.RichTextField()
    limitations = aristotle.models.RichTextField()
    where_to_get = aristotle.models.RichTextField()
    terms_of_use = aristotle.models.RichTextField()
    
    indicators = models.ManyToManyField(
        Indicator,
        related_name='instruments'
    )
