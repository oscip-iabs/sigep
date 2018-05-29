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

