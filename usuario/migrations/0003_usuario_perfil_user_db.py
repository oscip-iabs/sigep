# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-15 17:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '0002_notificacao_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario_perfil',
            name='user_db',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='USER'),
        ),
    ]
