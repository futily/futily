# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 20:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0002_auto_20170820_2211'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='squad',
            unique_together=set([]),
        ),
    ]
