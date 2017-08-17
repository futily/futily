# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 13:09
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_cardcollection_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardcollection',
            name='user',
            field=annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
