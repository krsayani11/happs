# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import forms.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendee_event', models.ForeignKey(default=None, to='events.UserEvents')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('user_id', models.BigIntegerField()),
                ('authentication_token', models.CharField(max_length=255)),
                ('datafile', models.ImageField(upload_to=forms.models.upload_to, null=True, verbose_name=b'image', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='attendees',
            name='username',
            field=models.ForeignKey(to='forms.User'),
        ),
    ]
