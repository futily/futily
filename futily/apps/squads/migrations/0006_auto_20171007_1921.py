# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-07 18:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0005_squadplayer_chemistry'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 10, 7, 18, 21, 59, 393333, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squad',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
