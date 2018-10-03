# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-03 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0018_parceiro_tipo_instrumento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceiro',
            name='existe_instrumento_formal',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'N\xe3o')], default='NAO', max_length=50, null=True, verbose_name='J\xe1 existe algum instrumento formal ?'),
        ),
        migrations.AlterField(
            model_name='parceiro',
            name='formaliza_parceria',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'N\xe3o')], default='NAO', max_length=50, null=True, verbose_name='\xc9 necess\xe1rio formaliza\xe7\xe3o de parceria ?'),
        ),
        migrations.AlterField(
            model_name='parceiro',
            name='tipo_instrumento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projeto.Tipo_Instrumento', verbose_name='Tipo de instrumento espec\xedfico.'),
        ),
        migrations.AlterField(
            model_name='tipo_instrumento',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
