# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritepokemon',
            name='shiny',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='favoritepokemon',
            name='charge_move',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='favoritepokemon',
            name='fast_move',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
