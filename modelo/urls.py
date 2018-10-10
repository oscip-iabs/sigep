# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.inicio_modelo, name='inicio'),
]