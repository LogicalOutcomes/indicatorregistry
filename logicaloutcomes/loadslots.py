import os,sys

settings = sys.argv[1]
slots_file = sys.argv[2]

print "loading django"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
import django
django.setup()

print settings
from aristotle_mdr.contrib.slots.models import Slot, SlotDefinition
from comet.models import Indicator

success = 0
failure = 0
slot_type,created = SlotDefinition.objects.get_or_create(
    app_label='comet',
    concept_type='indicator',
    slot_name='Instrument',
    cardinality = SlotDefinition.CARDINALITY.repeatable
)
print "starting"
with open(slots_file) as slots:
    for slot in slots:
        slot = slot.strip()
        short_name,value = slot.split(',')
        indicator = Indicator.objects.filter(short_name=short_name).first()
        if indicator:
            indicator.slots.all().delete()
            obj,created = Slot.objects.get_or_create(
                type=slot_type,
                concept=indicator,
                value=value
            )
            if created:
                print short_name,"exists, skipping"
            else:
                success += 1
        else:
            print short_name,"doesn't exist failure"
            failure += 1
print "Success =",success
print "Failure =",failure
