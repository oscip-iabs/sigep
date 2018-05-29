#_x -- coding: utf8 --
# vim: set fileencoding=utf8 :

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

from django.db import models

# Create your models here.


class Usuario_Perfil(models.Model):
	SEXO = (
		(0, 'Feminino'),
		(1, 'Masculino'),
	)

	date_created = models.DateTimeField(auto_now_add=True)
	nome = models.CharField(max_length=200, blank=True, null=True,verbose_name=u"Nome do usuario")
	cpf = models.CharField(max_length=14, unique=True, verbose_name=u"CPF")
	email = models.CharField(max_length=100, unique=True, verbose_name=u"E-mail")
	telefone = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"Telefone")
	idade = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Idade')
	sexo = models.IntegerField(default=0, blank=True, null=True, choices=SEXO, verbose_name=u'Genero')