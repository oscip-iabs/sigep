# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^adicionar_possibilidade/$', views.add_possibilidade, name='add_possibilidade'),
    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/dadosbasicos/$',views.cadastro_dados_basicos_possibilidade, name='cadastro_dados_basicos_possibilidade'),
    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/dadosfinanceiros/$',views.cadastro_dados_financeiros_possibilidade, name='cadastro_dados_financeiros_possibilidade'),
    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/dadosfinanciador/$',views.cadastro_dados_financiador_possibilidade, name='cadastro_dados_financiador_possibilidade'),


]
	