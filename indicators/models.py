from __future__ import unicode_literals
from django.db import models
import aristotle_mdr as aristotle
from comet.models import Indicator


class Instrument(aristotle.models.concept):
    template = "indicators/instrument.html"
    # population = models.ForeignKey(Population, null=True)
    population = aristotle.models.RichTextField()
    limitations = aristotle.models.RichTextField()
    where_to_get = aristotle.models.RichTextField()
    terms_of_use = aristotle.models.RichTextField()

    indicators = models.ManyToManyField(
        Indicator,
        related_name='instruments'
    )


class Goal(aristotle.models.concept):
    """
    On September 25th 2015, countries adopted a set of goals to end poverty,
    protect the planet, and ensure prosperity for all as part of a new sustainable development agenda.
    Each goal has specific targets to be achieved over the next 15 years. - http://www.un.org/sustainabledevelopment/sustainable-development-goals/
    """
    template = "indicators/goal.html"

    indicators = models.ManyToManyField(
        Indicator,
        related_name='related_goals'
    )
