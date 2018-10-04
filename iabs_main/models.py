#_x -- coding: utf8 --
# vim: set fileencoding=utf8 :
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

import os
import datetime

class Geral_Status(models.Model):
	cod_status 		= models.IntegerField(null=True, blank=True)
	previous_status = models.IntegerField(null=True, blank=True)
	next_status		= models.IntegerField(null=True, blank=True)

	referencia = models.CharField(max_length=1000, blank=True, null=True)
	chave      = models.CharField(max_length=1000, blank=True, null=True)
	texto      = models.CharField(max_length=1000, blank=True, null=True)

	def __str__(self):
		return self.texto.encode('utf-8').strip()


class Pais(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    nome_pt = models.CharField(max_length=150, blank=True, null=True)
    iso2 = models.CharField(max_length=150, blank=True, null=True)
    iso3 = models.CharField(max_length=150, blank=True, null=True)
    bacen = models.IntegerField(blank=True, null=True)

    def __str__(self):
        nome_pais = '[%s] %s' % (self.iso2, self.nome_pt)
        return nome_pais.encode('utf-8').strip()

class Regiao(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome.encode('utf-8').strip()


class Estado(models.Model):
    codigo_uf = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    regiao = models.ForeignKey(Regiao, blank=True, null=True)

    def __str__(self):
        nome_estado = '[%s] %s' % (self.uf, self.nome)
        return nome_estado.encode('utf-8').strip()


class Municipio(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    estado = models.ForeignKey(Estado, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    nome_estado = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        nome_municipio = '[%s] %s' % (self.uf, self.nome)
        return nome_municipio.encode('utf-8').strip()
