# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-16 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20171022_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='cached_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
