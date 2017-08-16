# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import futily.apps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0004_type_quality'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['order', '-is_online', 'ea_id']},
        ),
        migrations.RenameField(
            model_name='type',
            old_name='normal_types',
            new_name='roll_1_types',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='normal_types_count',
            new_name='roll_1_types_count',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='normal_types_rating_max',
            new_name='roll_1_types_rating_max',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='normal_types_rating_min',
            new_name='roll_1_types_rating_min',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='rare_types',
            new_name='roll_2_types',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='rare_types_count',
            new_name='roll_2_types_count',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='rare_types_rating_max',
            new_name='roll_2_types_rating_max',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='rare_types_rating_min',
            new_name='roll_2_types_rating_min',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='special_types',
            new_name='roll_3_types',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='special_types_count',
            new_name='roll_3_types_count',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='special_types_rating_max',
            new_name='roll_3_types_rating_max',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='special_types_rating_min',
            new_name='roll_3_types_rating_min',
        ),
        migrations.AddField(
            model_name='type',
            name='roll_4_types',
            field=futily.apps.fields.ChoiceArrayField(base_field=models.CharField(choices=[('', ''), ('award_winner', 'Award winner'), ('bronze', 'Bronze'), ('confederation_champions_motm', 'Confederation champions motm'), ('fut_birthday', 'Fut birthday'), ('futties_winner', 'Futties winner'), ('gold', 'Gold'), ('gotm', 'Gotm'), ('halloween', 'Halloween'), ('imotm', 'Imotm'), ('legend', 'Legend'), ('motm', 'Motm'), ('movember', 'Movember'), ('ones_to_watch', 'Ones to watch'), ('pink', 'Pink'), ('purple', 'Purple'), ('rare_bronze', 'Rare bronze'), ('rare_gold', 'Rare gold'), ('rare_silver', 'Rare silver'), ('record_breaker', 'Record breaker'), ('sbc_base', 'Sbc base'), ('silver', 'Silver'), ('st_patricks', 'St patricks'), ('tots_bronze', 'Tots bronze'), ('tots_gold', 'Tots gold'), ('tots_silver', 'Tots silver'), ('totw_bronze', 'Totw bronze'), ('totw_gold', 'Totw gold'), ('totw_silver', 'Totw silver'), ('toty', 'Toty')], max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_4_types_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_4_types_rating_max',
            field=models.PositiveIntegerField(default=99),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_4_types_rating_min',
            field=models.PositiveIntegerField(default=75),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_5_types',
            field=futily.apps.fields.ChoiceArrayField(base_field=models.CharField(choices=[('', ''), ('award_winner', 'Award winner'), ('bronze', 'Bronze'), ('confederation_champions_motm', 'Confederation champions motm'), ('fut_birthday', 'Fut birthday'), ('futties_winner', 'Futties winner'), ('gold', 'Gold'), ('gotm', 'Gotm'), ('halloween', 'Halloween'), ('imotm', 'Imotm'), ('legend', 'Legend'), ('motm', 'Motm'), ('movember', 'Movember'), ('ones_to_watch', 'Ones to watch'), ('pink', 'Pink'), ('purple', 'Purple'), ('rare_bronze', 'Rare bronze'), ('rare_gold', 'Rare gold'), ('rare_silver', 'Rare silver'), ('record_breaker', 'Record breaker'), ('sbc_base', 'Sbc base'), ('silver', 'Silver'), ('st_patricks', 'St patricks'), ('tots_bronze', 'Tots bronze'), ('tots_gold', 'Tots gold'), ('tots_silver', 'Tots silver'), ('totw_bronze', 'Totw bronze'), ('totw_gold', 'Totw gold'), ('totw_silver', 'Totw silver'), ('toty', 'Toty')], max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_5_types_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_5_types_rating_max',
            field=models.PositiveIntegerField(default=99),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_5_types_rating_min',
            field=models.PositiveIntegerField(default=75),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_6_types',
            field=futily.apps.fields.ChoiceArrayField(base_field=models.CharField(choices=[('', ''), ('award_winner', 'Award winner'), ('bronze', 'Bronze'), ('confederation_champions_motm', 'Confederation champions motm'), ('fut_birthday', 'Fut birthday'), ('futties_winner', 'Futties winner'), ('gold', 'Gold'), ('gotm', 'Gotm'), ('halloween', 'Halloween'), ('imotm', 'Imotm'), ('legend', 'Legend'), ('motm', 'Motm'), ('movember', 'Movember'), ('ones_to_watch', 'Ones to watch'), ('pink', 'Pink'), ('purple', 'Purple'), ('rare_bronze', 'Rare bronze'), ('rare_gold', 'Rare gold'), ('rare_silver', 'Rare silver'), ('record_breaker', 'Record breaker'), ('sbc_base', 'Sbc base'), ('silver', 'Silver'), ('st_patricks', 'St patricks'), ('tots_bronze', 'Tots bronze'), ('tots_gold', 'Tots gold'), ('tots_silver', 'Tots silver'), ('totw_bronze', 'Totw bronze'), ('totw_gold', 'Totw gold'), ('totw_silver', 'Totw silver'), ('toty', 'Toty')], max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_6_types_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_6_types_rating_max',
            field=models.PositiveIntegerField(default=99),
        ),
        migrations.AddField(
            model_name='type',
            name='roll_6_types_rating_min',
            field=models.PositiveIntegerField(default=75),
        ),
    ]
