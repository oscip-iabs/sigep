# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from models import Projeto, Nucleo, Nucleo_x_Projeto

admin.site.register(Projeto)
admin.site.register(Nucleo_x_Projeto)
admin.site.register(Nucleo)
