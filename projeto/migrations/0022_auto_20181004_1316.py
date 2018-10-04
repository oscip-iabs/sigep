# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-04 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0021_auto_20181003_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='localizacao_mundial',
            field=models.IntegerField(blank=True, choices=[(0, 'Nacional'), (1, 'Internacional'), (2, 'Regional'), (3, 'Estadual'), (4, 'Municipal')], null=True, verbose_name='Area de Abrangencia'),
        ),
    ]
