# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('comet', '0007_promote_framework_to_concept'),
        ('aristotle_mdr', '0012_better_workflows'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('_concept_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aristotle_mdr._concept')),
                ('short_name', models.CharField(max_length=100, blank=True)),
                ('version', models.CharField(max_length=20, blank=True)),
                ('synonyms', models.CharField(max_length=200, blank=True)),
                ('references', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('origin_URI', models.URLField(help_text='If imported, the original location of the item', blank=True)),
                ('comments', ckeditor_uploader.fields.RichTextUploadingField(help_text='Descriptive comments about the metadata item.', blank=True)),
                ('submitting_organisation', models.CharField(max_length=256, blank=True)),
                ('responsible_organisation', models.CharField(max_length=256, blank=True)),
                ('population', ckeditor_uploader.fields.RichTextUploadingField()),
                ('limitations', ckeditor_uploader.fields.RichTextUploadingField()),
                ('where_to_get', ckeditor_uploader.fields.RichTextUploadingField()),
                ('terms_of_use', ckeditor_uploader.fields.RichTextUploadingField()),
                ('indicators', models.ManyToManyField(related_name='instruments', to='comet.Indicator')),
                ('superseded_by', models.ForeignKey(related_name='supersedes', blank=True, to='logicaloutcomes.Instrument', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('aristotle_mdr._concept',),
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indicator', models.ForeignKey(related_name='populations', to='comet.Indicator')),
                ('object_class', models.ForeignKey(to='aristotle_mdr.ObjectClass')),
            ],
        ),
    ]
