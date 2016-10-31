# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('comet', '0001_squashed_0008_fix_concept_fields'),
        ('aristotle_mdr', '0017_add_organisations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('_concept_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aristotle_mdr._concept')),
                ('indicators', models.ManyToManyField(related_name='related_goals', to='comet.Indicator')),
            ],
            options={
                'abstract': False,
            },
            bases=('aristotle_mdr._concept',),
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('_concept_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aristotle_mdr._concept')),
                ('population', ckeditor_uploader.fields.RichTextUploadingField()),
                ('limitations', ckeditor_uploader.fields.RichTextUploadingField()),
                ('where_to_get', ckeditor_uploader.fields.RichTextUploadingField()),
                ('terms_of_use', ckeditor_uploader.fields.RichTextUploadingField()),
                ('indicators', models.ManyToManyField(related_name='instruments', to='comet.Indicator')),
            ],
            options={
                'abstract': False,
            },
            bases=('aristotle_mdr._concept',),
        ),
    ]
