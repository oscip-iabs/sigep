# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-14 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0005_auto_20180511_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='check_possibilidade_cadastro_basico',
            field=models.NullBooleanField(default=False),
        ),
    ]
