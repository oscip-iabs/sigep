#_x -- coding: utf8 --
# vim: set fileencoding=utf8 :

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Usuario_Perfil(models.Model):
    SEXO = (
        (0, 'Feminino'),
        (1, 'Masculino'),
    )

    date_created = models.DateTimeField(auto_now_add=True)
    nome 		= models.CharField(max_length=200, blank=True, null=True,verbose_name=u"Nome do usuario")
    cpf 		= models.CharField(max_length=14, unique=True, verbose_name=u"CPF")
    email 		= models.CharField(max_length=100, unique=True, verbose_name=u"E-mail")
    telefone 	= models.CharField(max_length=100, blank=True, null=True, verbose_name=u"Telefone")
    idade 		= models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Idade')
    sexo 		= models.IntegerField(default=0, blank=True, null=True, choices=SEXO, verbose_name=u'Genero')
    user_db     = models.ForeignKey(User, verbose_name=u'USER', blank=True, null=True)

    def __str__(self):
        return self.nome.encode('utf-8').strip()


class Notificacao_Usuario(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200, blank=True, null=True,verbose_name=u"Titulo")
    descricao = models.CharField(max_length=500, unique=True, verbose_name=u"Descricao")
    tipo = models.CharField(max_length=14, unique=True, verbose_name=u"Tipo")
    visualizada = models.BooleanField(default=False, verbose_name=u"Recomposição da Mata Ciliar")
    referencia = models.IntegerField(null=True, blank=True, verbose_name=u"Projeto id")

    def __str__(self):
        return self.titulo.encode('utf-8').strip()