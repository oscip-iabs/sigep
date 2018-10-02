#_x -- coding: utf8 --
# vim: set fileencoding=utf8 :

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

from iabs_main.models import Geral_Status
from usuario.models import Usuario_Perfil

import os
import datetime


class Abrangencia_Atuacao(models.Model):
    date_created    = models.DateTimeField(auto_now_add=True)
    texto           = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u'Área de atuação do projeto')
    descricao       = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u'Descrição da área de atuação')

    def __str__(self):
        return self.texto.encode('utf-8').strip()


class Tipo_Contratacao(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    texto        = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.texto.encode('utf-8').strip()


class Projeto(models.Model):
    LOCAL_GLOBAL = (
        (0, 'Nacional'),
        (1, 'Internacional'),
        (2, 'Regional'),
        (3, 'Estadual'),
        (4, 'Municipal'),
    )

    PRIORIDADE_PROJETO = (
        (0, 'Alta'),
        (1, 'Média'),
        (2, 'Baixa'),
    )

    date_created        = models.DateTimeField(auto_now_add=True)
    titulo              = models.CharField(max_length=1000, blank=True, null=True,  verbose_name=u'Descreva o título/Objetivo')
    apoiador            = models.CharField(max_length=1000, blank=True, null=True,  verbose_name=u'Instituição financiadora ou possível apoiador')
    chave               = models.CharField(max_length=15,   blank=True, null=True)
    valor_estimado      = models.CharField(max_length=1000, blank=True, null=True,  verbose_name=u'Valor estimado', help_text=u'Valor em R$')
    tema_possibilidade  = models.CharField(max_length=1000, blank=True, null=True,  verbose_name=u'Descreva o tema')
    prazo_limite        = models.DateField(default=datetime.date.today, blank=True, verbose_name=u'Data da publicação')
    descricao           = models.TextField(max_length=5000, blank=True, null=True,  verbose_name=u'Descrição resumida')
    periodo_execucao    = models.IntegerField(null=True, blank=True, verbose_name=u'Informe o período em meses.')
    previsao_resultado  = models.DateField(default=datetime.date.today, blank=True, verbose_name=u'Data da previsão do resultado')
    tipo_contratacao    = models.ForeignKey(Tipo_Contratacao, null=True, verbose_name=u'Tipo da contratação')

    status              = models.ForeignKey(Geral_Status, blank=True, null=True)

    check_possibilidade_cadastro_basico      = models.NullBooleanField(default=False, blank=True)
    check_possibilidade_cadastro_financeiro  = models.NullBooleanField(default=False, blank=True)
    check_possibilidade_cadastro_nucleo      = models.NullBooleanField(default=False, blank=True)
    check_possibilidade_cadastro_localizacao = models.NullBooleanField(default=False, blank=True)

    check_projeto_potencial_cadastro_basico = models.NullBooleanField(default=False, blank=True)
    check_projeto_potencial_cadastro_financeiro = models.NullBooleanField(default=False, blank=True)
    check_projeto_potencial_cadastro_nucleo = models.NullBooleanField(default=False, blank=True)
    check_projeto_potencial_cadastro_localizacao = models.NullBooleanField(default=False, blank=True)
    check_projeto_potencial_cadastro_documento = models.NullBooleanField(default=False, blank=True)
    check_projeto_potencial_cadastro_parceiro = models.NullBooleanField(default=False, blank=True)

    localizacao_mundial     = models.IntegerField(null=False, default=0, verbose_name=u'Localização da possibilidade', choices=LOCAL_GLOBAL)
    localizacao_descricao   = models.TextField(max_length=5000, blank=True, null=True, verbose_name=u'Outras informações em relação a localização')
    localizacao_abrangencia = models.ForeignKey(Abrangencia_Atuacao, null=True)

    prioridade_projeto       = models.IntegerField(null=False, default=0, verbose_name=u'Prioridade do Projeto', choices=PRIORIDADE_PROJETO)
    justificativa_prioridade = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u'Justificativa da Prioridade')

    possibilidade_responsavel = models.ForeignKey(Usuario_Perfil, null=True)


class Nucleo(models.Model):
    date_created    = models.DateTimeField(auto_now_add=True)
    texto           = models.CharField(max_length=1000, blank=True, null=True)
    responsavel     = models.ForeignKey(Usuario_Perfil)

    def __str__(self):
        return self.texto.encode('utf-8').strip()


class Nucleo_x_Projeto(models.Model):
    date_created    = models.DateTimeField(auto_now_add=True)
    projeto         = models.ForeignKey(Projeto, blank=True, null=True)
    nucleo          = models.ForeignKey(Nucleo, null=True)


class Avaliacao_Possibilidade(models.Model):
    CATEGORIA_ADEQUACAO = (
        (0, 'Informações Básicas'),
        (1, 'Informaçoes Finaceiras'),
        (2, 'Núcleos'),
        (3, 'Area de Atuação'),
    )

    date_created = models.DateTimeField(auto_now_add=True)
    adequacao = models.TextField(max_length=5000, blank=True, null=True, verbose_name=u'Descrição resumida')
    categoria = models.IntegerField(null=False, blank=True, default=0, verbose_name=u'Categoria da adequação', choices=CATEGORIA_ADEQUACAO)
    projeto = models.ForeignKey(Projeto, blank=True, null=True)
    user_avaliador = models.ForeignKey(Usuario_Perfil, blank=True, null=True)


class Contato(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    nome         = models.CharField(max_length=100, blank=True, null=True)
    email        = models.CharField(max_length=100, blank=True, null=True)
    telefone     = models.CharField(max_length=30, blank=True, null=True)
    info_contato = models.CharField(max_length=100, blank=True, null=True)
    projeto      = models.ForeignKey(Projeto, blank=True, null=True)

    def __str__(self):
        return self.nome.encode('utf-8').strip()


class Equipe_Projeto(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    participante = models.ForeignKey(Usuario_Perfil, blank=True, null=True)
    projeto      = models.ForeignKey(Projeto, blank=True, null=True)
    responsabilidade = models.CharField(max_length=100, blank=True, null=True)


class Documento(models.Model):
    TIPO_DOCUMENTO = (
        (0, 'Edital'),
        (1, 'Outros'),
    )

    date_created = models.DateTimeField(auto_now_add=True)
    nome         = models.CharField(max_length=100, blank=True, null=True)
    link         = models.CharField(max_length=100, blank=True, null=True)
    tipo         = models.IntegerField(null=False, blank=True, default=0, verbose_name=u'Tipo do documento potencial', choices=TIPO_DOCUMENTO)
    projeto      = models.ForeignKey(Projeto, blank=True, null=True)

    def __str__(self):
        return self.nome.encode('utf-8').strip()


class Parceiro(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    nome         = models.CharField(max_length=100, blank=True, null=True)
    telefone     = models.CharField(max_length=100, blank=True, null=True)
    email        = models.CharField(max_length=100, blank=True, null=True)
    projeto      = models.ForeignKey(Projeto, blank=True, null=True)

    def __str__(self):
        return self.nome.encode('utf-8').strip()


class Historico_Projeto(models.Model):
    date_created     = models.DateTimeField(auto_now_add=True)
    date_modificacao = models.DateField(default=datetime.date.today)
    texto            = models.CharField(max_length=1000, blank=True, null=True)
    tipo             = models.CharField(max_length=1000, blank=True, null=True)
    projeto          = models.ForeignKey(Projeto)
    modified_user    = models.ForeignKey(Usuario_Perfil, null=True)
