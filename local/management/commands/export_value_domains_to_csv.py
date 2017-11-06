import unicodecsv

from .export_data_elements_to_csv import Command as ExportValueDomainsCommand
from aristotle_mdr.models import ValueDomain


class Command(ExportValueDomainsCommand):
    help = 'Export Value domains to CSV'

    def handle(self, *args, **options):
        writer = unicodecsv.writer(options.get('csv_file'), encoding='utf-8')
        # header
        writer.writerow((
            'ID',
            'Code',
            'Short name',
            'Name',
            'Value',
            'Meaning',
        ))
        # rows
        for vd in ValueDomain.objects.all():
            # Permissible Values of the Value Domain
            for pv in vd.permissibleValues:
                writer.writerow((
                    vd.id,
                    self.get_code(vd),
                    vd.short_name,
                    vd.name,
                    pv.value,
                    pv.meaning,
                ))
            # Empty Value Domain
            if not vd.permissibleValues:
                writer.writerow((
                    vd.id,
                    self.get_code(vd),
                    vd.short_name,
                    vd.name,
                    None,
                    None,
                ))
        self.stdout.write('Successfully exported {} Value domains'.format(ValueDomain.objects.count()))
