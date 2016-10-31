from django.contrib import admin
from logicaloutcomes.models import Instrument, Goal
from aristotle_mdr.register import register_concept

register_concept(Instrument)
register_concept(Goal)
