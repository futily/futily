# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-22 20:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0018_auto_20171022_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='rating_ibra',
            new_name='rating_attacking',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='rating_pirlo',
            new_name='rating_creative',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='rating_vidic',
            new_name='rating_defensive',
        ),
        migrations.AddField(
            model_name='player',
            name='rating_anchor',
            field=models.PositiveIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
    ]
