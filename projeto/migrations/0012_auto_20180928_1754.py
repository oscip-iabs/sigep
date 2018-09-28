# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-28 17:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0011_auto_20180928_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Contratacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('texto', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='projeto',
            name='previsao_resultado',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Data da previs\xe3o do resultado'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='tipo_contratacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projeto.Tipo_Contratacao', verbose_name='Tipo da contrata\xe7\xe3o'),
        ),
    ]
