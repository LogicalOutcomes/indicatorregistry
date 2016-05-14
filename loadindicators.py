import datetime
import os,sys
import csv
reload(sys)
sys.setdefaultencoding("utf-8")

settings = sys.argv[1]
csv_file = sys.argv[2]
vd_file = sys.argv[3]

print("loading django")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
import django
django.setup()


from aristotle_mdr.contrib.slots.models import Slot, SlotDefinition
from aristotle_mdr import models 
from comet import models as comet
from logicaloutcomes import models as lo_models

lo,c = models.RegistrationAuthority.objects.get_or_create(name="Logical Outcomes")
wg,c = models.Workgroup.objects.get_or_create(name="Import Workgroup")
wg.registrationAuthorities=[lo]
user = models.RegistrationAuthority.objects.get_or_create(name="Logical Outcomes")

slots = dict()
slot_columns = [
    (u'Indicator Code:','Code',''),
    (u'Citation instruction:','Citation instruction','How to cite this document'),
    (u'Usage instruction:','Usage instruction','How to use this document'),
    (u'Method of Measurement 1:','Method of Measurement',''),
    (u'Method of Measurement 2:','Method of Measurement',''),
    (u'Data Collection Frequency 1:','Data Collection Frequency',''),
    (u'Data Collection Frequency 2:','Data Collection Frequency',''),
    (u'Data Collection Frequency 3:','Data Collection Frequency',''),
    (u'Data Source:','Data Source',''),
    ('Instrument:','Instrument',''),
    ('DOI:','DOI',''),
    ('Universe:','Universe','')
]
for sl in slot_columns:
    sl,name,desc = sl
    slot_type,created = SlotDefinition.objects.get_or_create(
        app_label='comet',
        concept_type='indicator',
        slot_name=name,
        cardinality = SlotDefinition.CARDINALITY.repeatable
    )
    slots[sl]=slot_type
print slots

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel_tab, reader=csv.DictReader, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    return csv_reader

def lb_2_p(txt):
    if "\n\n" in txt:
        return "<p>"+"</p><p>".join(txt.split("\n\n"))+"</p>"
    else:
        return txt

import re
def jpger(txt):
    txt = re.sub(r"(https?://.*?jpg)", "<img src='\\1'>", txt)
    return txt

print("starting")
with open(csv_file,'rb') as csvfile:
    reader = unicode_csv_reader(csvfile)
    for row in reader:
        name = row[u"Indicator Name:"].strip()
        if name == "":
            continue 
        defaults = {
            "workgroup": wg,
            "short_name": row["Short name:"],
            "definition": row["Purpose:"],
            "references": row["References:"],
            "rationale": lb_2_p(row["Interpretation:"]),
            "numerator_description": lb_2_p(row["Numerator:"]),
            "denominator_description": lb_2_p(row["Denominator:"]),
            "disaggregation_description": lb_2_p(row["Disaggregation(s) 1:"])+lb_2_p(row["Disaggregation(s) 2:"]),
        }
        indicator = comet.Indicator.objects.create(
            name=name,
            **defaults
        )
        print indicator.pk, indicator.name #row.keys()
        models.Status.objects.get_or_create(
            concept=indicator,
            registrationAuthority=lo,
            registrationDate=datetime.date(2009, 4, 28),
            state=models.STATES.standard
        )

        for sl in slot_columns:
            sl,name,desc = sl
            value = row[sl]
            obj,created = Slot.objects.get_or_create(
                type=slots[sl],
                concept=indicator,
                value=jpger(value)
            )
        
        # set relevant populations
        # populations = row["Universe:"].split(';')
        # for pop in populations:
        #     pop = pop.strip()
        #     if pop == "":
        #         continue 
        #     pop, create = models.ObjectClass.objects.get_or_create(
        #         name = pop,
        #         defaults = {
        
        #             "workgroup": wg,
        #             "definition": "",
        #         }
        #     )
        #     models.Status.objects.get_or_create(
        #         concept=pop,
        #         registrationAuthority=lo,
        #         registrationDate=datetime.date(2009, 4, 28),
        #         state=models.STATES.standard
        #     )
        #     pop, c = lo_models.Population.objects.get_or_create(object_class=pop,indicator=indicator)
        
        
        # set outcomes
        outcomes = row["Indicator group:"].split(';')
        for outcome in outcomes:
            outcome = outcome.strip()
            if outcome == "":
                continue 
            outcome, created = comet.OutcomeArea.objects.get_or_create(
                name = outcome,
                defaults = {
                    "workgroup": wg,
                    "definition": "",
                }
            )
            if created:
                models.Status.objects.get_or_create(
                    concept=outcome,
                    registrationAuthority=lo,
                    registrationDate=datetime.date(2009, 4, 28),
                    state=models.STATES.standard
                )
            indicator.outcome_areas.add(outcome)

        # set outcomes
        frameworks = row["Framework:"].split(';')
        for framework in frameworks:
            framework = framework.strip()
            if framework == "":
                continue 
            framework, created = comet.Framework.objects.get_or_create(
                name = framework,
                defaults = {
                    "workgroup": wg,
                    "definition": "",
                }
            )
            if created:
                models.Status.objects.get_or_create(
                    concept=framework,
                    registrationAuthority=lo,
                    registrationDate=datetime.date(2009, 4, 28),
                    state=models.STATES.standard
                )
            framework.indicators.add(indicator)

        if created:
            models.Status.objects.get_or_create(
                concept=framework,
                registrationAuthority=lo,
                registrationDate=datetime.date(2009, 4, 28),
                state=models.STATES.standard
            )
        framework.indicators.add(indicator)
        
with open(vd_file,'rb') as csvfile:
    #vds = csvfile.read().split('\n\t\t\t\n')
    val_dom = None
    indicator = None
    n = 0
    for i,row in enumerate(unicode_csv_reader(csvfile,reader=csv.reader)):
        if val_dom is None:
            ind_code = row[0]
            vd_name = row[1]
            meaning = row[2]
            value = row[3]
            dt = models.DataType.objects.get(name='Number')
            val_dom, created = models.ValueDomain.objects.get_or_create(
                    name = vd_name,
                    defaults = {
                        "workgroup": wg,
                        "definition": "Imported from the Indicator Reference Sheet",
                        "data_type": dt,
                    }
                )
            models.Status.objects.get_or_create(
                concept=val_dom,
                registrationAuthority=lo,
                registrationDate=datetime.date(2009, 4, 28),
                state=models.STATES.standard
            )
            indicator = comet.Indicator.objects.filter(slots__type=slots['Indicator Code:'],slots__value=ind_code).first()
            if indicator:
                indicator.valueDomain = val_dom
                indicator.save()
            else:
                print "No indicator - ", ind_code
            models.PermissibleValue.objects.create(valueDomain=val_dom,value=value,meaning=meaning,order=n)
            n += 1
        elif row == ['','','','']:
            if n == 0:
                val_dom.permssible_values.delete()
            val_dom = None
            indicator = None
            n = 0
        else:
            meaning = row[2]
            value = row[3]
            models.PermissibleValue.objects.create(valueDomain=val_dom,value=value,meaning=meaning,order=n)
            n += 1
