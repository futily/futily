# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 15:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='following', through='users.UserFollowers', to=settings.AUTH_USER_MODEL),
        ),
    ]
