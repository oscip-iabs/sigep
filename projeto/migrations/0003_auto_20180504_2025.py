# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-04 20:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0002_auto_20180503_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico_Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modificacao', models.DateField(default=datetime.date.today)),
                ('texto', models.CharField(blank=True, max_length=1000, null=True)),
                ('modified_user', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='projeto',
            name='modified_user',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='localizacao_mundial',
            field=models.IntegerField(blank=True, choices=[(0, 'Nacional'), (1, 'Internacional'), (2, 'Regional'), (3, 'Estadual'), (4, 'Municipal')], null=True, verbose_name='Localiza\xe7\xe3o da possibilidade'),
        ),
        migrations.AddField(
            model_name='historico_projeto',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projeto.Projeto'),
        ),
    ]
