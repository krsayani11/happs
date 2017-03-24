# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileupload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('event_id', models.IntegerField()),
                ('datafile', models.ImageField(upload_to=upload.models.upload_to, null=True, verbose_name='image', blank=True)),
                ('username', models.ForeignKey(default=None, to='forms.user')),
            ],
        ),
    ]
