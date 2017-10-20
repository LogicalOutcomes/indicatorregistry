import argparse
import unicodecsv

from django.core.management.base import BaseCommand
from aristotle_mdr.models import DataElement
from indicators.templatetags.logicaltags import get_single_slot


class Command(BaseCommand):
    help = 'Export Data Elements to CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=argparse.FileType('wb'))

    def get_slot(self, concept, slots):
        for slot in slots:
            slot = get_single_slot(concept, slot).first()
            if slot and slot.value:
                return slot.value
        return None

    def handle(self, *args, **options):
        writer = unicodecsv.writer(options.get('csv_file'), encoding='utf-8')
        # header
        writer.writerow((
            'ID',
            'Short name',
            'Name',
            'Definition',
            'Value type',
            'Form name',
            'Value domain',
        ))
        # rows
        for de in DataElement.objects.all():
            writer.writerow((
                de.id,
                de.short_name,
                de.name,
                de.definition,
                self.get_slot(de, ['Value type']),
                self.get_slot(de, ['Form name', 'Form name EN']),
                de.valueDomain.pk if de.valueDomain else None,
            ))

        self.stdout.write('Successfully exported {} Data Elements'.format(DataElement.objects.count()))
