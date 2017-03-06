# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userevents',
            name='host',
            field=models.ForeignKey(related_name='for_host', default=None, to='forms.User'),
        ),
    ]
