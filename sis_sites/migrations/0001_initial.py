# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('value', models.TextField(null=True, blank=True)),
                ('order', models.IntegerField(default=0)),
                ('page', models.ForeignKey(to='flatpages.FlatPage')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name_plural': 'Content Blocks',
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=128)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Snippets',
            },
        ),
        migrations.AddField(
            model_name='contentblock',
            name='snippet',
            field=models.ForeignKey(to='sis_sites.Snippet'),
        ),
    ]
