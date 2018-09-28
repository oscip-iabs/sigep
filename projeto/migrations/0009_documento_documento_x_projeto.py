# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-27 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0008_auto_20180927_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo', models.IntegerField(blank=True, choices=[(0, 'Edital'), (1, 'Outros')], default=0, verbose_name='Tipo do documento potencial')),
            ],
        ),
        migrations.CreateModel(
            name='Documento_x_Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('documento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projeto.Documento')),
                ('projeto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projeto.Projeto')),
            ],
        ),
    ]
