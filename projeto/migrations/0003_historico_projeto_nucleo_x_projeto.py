# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-08 19:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('projeto', '0002_projeto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico_Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modificacao', models.DateField(default=datetime.date.today)),
                ('texto', models.CharField(blank=True, max_length=1000, null=True)),
                ('tipo', models.CharField(blank=True, max_length=1000, null=True)),
                ('modified_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario_Perfil')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projeto.Projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Nucleo_x_Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('nucleo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projeto.Nucleo')),
                ('projeto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projeto.Projeto')),
            ],
        ),
    ]