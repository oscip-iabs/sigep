# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-03 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geral_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('referencia', models.CharField(blank=True, max_length=1000, null=True)),
                ('chave', models.CharField(blank=True, max_length=1000, null=True)),
                ('texto', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
