# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-27 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0009_documento_documento_x_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='check_projeto_potencial_cadastro_documento',
            field=models.NullBooleanField(default=False),
        ),
    ]
