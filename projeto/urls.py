# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.inicio_projeto, name='inicio'),
    url(r'^adicionar_possibilidade/$', views.add_possibilidade, name='add_possibilidade'),
    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/dadosbasicos/$',views.cadastro_dados_basicos_possibilidade, name='cadastro_dados_basicos_possibilidade'),
    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/dadosfinanceiros/$',views.cadastro_dados_financeiros_possibilidade, name='cadastro_dados_financeiros_possibilidade'),
    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/nucleo/$',views.cadastro_nucleo_possibilidade, name='cadastro_nucleo_possibilidade'),
    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/localizacao/$',views.cadastro_localizacao_possibilidade, name='cadastro_localizacao_possibilidade'),
    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/finalizar/$',views.cadastro_finalizar_possibilidade, name='cadastro_finalizar_possibilidade'),

    url(r'^(?P<id_pos>[-\w\d]+)/possibilidade/(?P<chave_pos>[-\w\d]+)/avaliar/$',views.avaliar_possibilidade, name='avaliar_possibilidade'),
    url(r'^(?P<id_pos>[-\w\d]+)/possibilidade/(?P<chave_pos>[-\w\d]+)/aprovar/$',views.aprovar_possibilidade, name='aprovar_possibilidade'),

    url(r'^potencial/$', views.projeto_potencial, name='projeto_potencia'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/dadosbasicos/$', views.projeto_potencial_dadosbasicos, name='projeto_potencial_dadosbasicos'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/dadosfinanceiros/$', views.projeto_potencial_dadosfinanceiros, name='projeto_potencial_dadosfinanceiros'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/nucleo/$', views.projeto_potencial_nucleo, name='projeto_potencial_nucleo'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/localizacao/$', views.projeto_potencial_localizacao, name='projeto_potencial_localizacao'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/documentos/$', views.projeto_potencial_documentos, name='projeto_potencial_documentos'),

]