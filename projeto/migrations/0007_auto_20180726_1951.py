# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-26 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0006_auto_20180726_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao_possibilidade',
            name='categoria',
            field=models.IntegerField(blank=True, choices=[(0, 'Informa\xe7\xf5es B\xe1sicas'), (1, 'Informa\xe7oes Finaceiras'), (2, 'N\xfacleos'), (3, 'Area de Atua\xe7\xe3o')], default=0, verbose_name='Categoria da adequa\xe7\xe3o'),
        ),
    ]
