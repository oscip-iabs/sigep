#_x -- coding: utf8 --
# vim: set fileencoding=utf8 :

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

from iabs_main.models import Geral_Status
from usuario.models import Usuario_Perfil

import os
import datetime

class Nucleo(models.Model):
    date_created    = models.DateTimeField(auto_now_add=True)
    texto           = models.CharField(max_length=1000, blank=True, null=True)
    responsavel     = models.ForeignKey(Usuario_Perfil)

    def __str__(self):
        return self.texto


class Projeto(models.Model):
    LOCAL_GLOBAL = (
        (0, 'Nacional'),
        (1, 'Internacional'),
        (2, 'Regional'),
        (3, 'Estadual'),
        (4, 'Municipal'),
    )

    date_created        = models.DateTimeField(auto_now_add=True)
    titulo              = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u'Descreva o título/Objetivo')
    apoiador            = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u'Instituição financiadora ou possível apoiador')
    chave               = models.CharField(max_length=15,   blank=True, null=True)
    valor_estimado      = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u'Valor estimado', help_text=u'Valor em R$')
    tema_possibilidade  = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u'Descreva o tema')
    prazo_limite        = models.DateField(default=datetime.date.today, blank=True, verbose_name=u'Data da publicação')
    descricao           = models.TextField(max_length=5000, blank=True, null=True, verbose_name=u'Descrição resumida')    
    periodo_execucao    = models.IntegerField(null=True,    blank=True, verbose_name=u'Informe o período em meses.')

    status              = models.ForeignKey(Geral_Status, blank=True)

    check_possibilidade_cadastro_basico      = models.NullBooleanField(default=False, blank=True)
    check_possibilidade_cadastro_financeiro  = models.NullBooleanField(default=False, blank=True)
    check_possibilidade_cadastro_financiador = models.NullBooleanField(default=False, blank=True)
    check_possibilidade_cadastro_localizacao = models.NullBooleanField(default=False, blank=True)

    localizacao_mundial = models.IntegerField(null=True, blank=True, verbose_name=u'Localização da possibilidade', choices=LOCAL_GLOBAL)
    fk_nucleo = models.ManyToManyField(Nucleo, through='Nucleo_Projeto', verbose_name=u'Nucleos do projeto', blank=True)

class Nucleo_Projeto(models.Model):
    fk_projeto  = models.ForeignKey(Projeto)
    fk_nucleo   = models.ForeignKey(Nucleo)


class Historico_Projeto(models.Model):
    date_created        = models.DateTimeField(auto_now_add=True)
    date_modificacao    = models.DateField(default=datetime.date.today)
    texto               = models.CharField(max_length=1000, blank=True, null=True)
    projeto             = models.ForeignKey(Projeto)
    modified_user       = models.CharField(max_length=500,  blank=True, null=True)
