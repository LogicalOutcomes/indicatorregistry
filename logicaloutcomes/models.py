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
