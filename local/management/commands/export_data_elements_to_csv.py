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

    def get_code(self, concept):
        res = []
        for ident in concept.identifiers.all():
            res.append(ident.identifier)
        if res:
            return u', '.join(res)
        else:
            return concept.id

    def handle(self, *args, **options):
        writer = unicodecsv.writer(options.get('csv_file'), encoding='utf-8')
        # header
        writer.writerow((
            'ID',
            'Code',
            'Short name',
            'Name',
            'Definition',
            'Value type',
            'Form name',
            'Terms of use',
            'Value domain',
        ))
        # rows
        for de in DataElement.objects.all():
            writer.writerow((
                de.id,
                self.get_code(de),
                de.short_name,
                de.name,
                de.definition,
                self.get_slot(de, ['Value type']),
                self.get_slot(de, ['Form name', 'Form name EN']),
                self.get_slot(de, ['Terms of use']),
                self.get_code(de.valueDomain) if de.valueDomain else None,
            ))

        self.stdout.write('Successfully exported {} Data Elements'.format(DataElement.objects.count()))
