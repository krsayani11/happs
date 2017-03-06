# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('description', models.TextField()),
                ('longitude', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('datafile', models.ImageField(upload_to=events.models.upload_to, null=True, verbose_name='image', blank=True)),
            ],
        ),
    ]
