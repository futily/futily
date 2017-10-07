# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0015_auto_20170921_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='color',
            field=models.CharField(
                choices=[
                    ('bronze',
                     'Bronze'),
                    ('silver',
                     'Silver'),
                    ('gold',
                     'Gold'),
                    ('rare_bronze',
                     'Rare bronze'),
                    ('rare_silver',
                     'Rare silver'),
                    ('rare_gold',
                     'Rare gold'),
                    ('legend',
                     'Legend'),
                    ('award_winner',
                     'Award Winner'),
                    ('confederation_champions_motm',
                     'Confederation Champions MOTM'),
                    ('europe_motm',
                     'Europe MOTM'),
                    ('fut_birthday',
                     'FUT Birthday'),
                    ('fut_champions_bronze',
                     'FUT Champions Bronze'),
                    ('fut_champions_gold',
                     'FUT Champions Gold'),
                    ('fut_champions_silver',
                     'FUT Champions Silver'),
                    ('fut_championship',
                     'FUT Championship'),
                    ('fut_mas',
                     'FUT Mas'),
                    ('fut_united',
                     'FUT United'),
                    ('futties_winner',
                     'Futties Winner'),
                    ('gotm',
                     'GOTM'),
                    ('halloween',
                     'Halloween'),
                    ('imotm',
                     'iMOTM'),
                    ('marquee',
                     'Marquee'),
                    ('motm',
                     'MOTM'),
                    ('movember',
                     'Movember'),
                    ('ones_to_watch',
                     'Ones To Watch'),
                    ('pink',
                     'Pink'),
                    ('purple',
                     'Purple'),
                    ('record_breaker',
                     'Record Breaker'),
                    ('rtr_contender',
                     'RTR Contender'),
                    ('rtr_gold',
                     'RTR Gold'),
                    ('sbc_base',
                     'SBC Base'),
                    ('sbc_premium',
                     'SBC Premium'),
                    ('st_patricks',
                     'St. Patricks'),
                    ('teal',
                     'teal'),
                    ('tots_bronze',
                     'TOTS Bronze'),
                    ('tots_gold',
                     'TOTS Gold'),
                    ('tots_silver',
                     'TOTS Silver'),
                    ('totw_bronze',
                     'TOTW Bronze'),
                    ('totw_gold',
                     'TOTW Gold'),
                    ('totw_silver',
                     'TOTW Silver'),
                    ('toty',
                     'TOTY')],
                max_length=100,
                null=True),
        ),
    ]
