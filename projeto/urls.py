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
    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/nucleo/delete/(?P<id_nucleo>[-\w\d]+)$',views.delete_possibilidade_nucleo, name='delete_possibilidade_nucleo'),

    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/localizacao/$',views.cadastro_localizacao_possibilidade, name='cadastro_localizacao_possibilidade'),

    # url(r'^(?P<id_pos>[-\w\d]+)/(?P<chave_pos>[-\w\d]+)/localizacao/save/estado$',views.localizacao_save_estado, name='localizacao_save_estado'),
    # url(r'^(?P<id_pos>[-\w\d]+)/(?P<chave_pos>[-\w\d]+)/localizacao/save/regiao$',views.localizacao_save_regiao, name='localizacao_save_regiao'),
    # url(r'^(?P<id_pos>[-\w\d]+)/(?P<chave_pos>[-\w\d]+)/localizacao/save/municipio$',views.localizacao_save_municipio, name='localizacao_save_municipio'),
    # url(r'^(?P<id_pos>[-\w\d]+)/(?P<chave_pos>[-\w\d]+)/localizacao/save/pais$',views.localizacao_save_pais, name='localizacao_save_pais'),
    #

    url(r'^(?P<id_pos>[-\w\d]+)/cadastro/(?P<chave_pos>[-\w\d]+)/finalizar/$',views.cadastro_finalizar_possibilidade, name='cadastro_finalizar_possibilidade'),

    url(r'^(?P<id_pos>[-\w\d]+)/possibilidade/(?P<chave_pos>[-\w\d]+)/avaliar/$',views.avaliar_possibilidade, name='avaliar_possibilidade'),
    url(r'^(?P<id_pos>[-\w\d]+)/possibilidade/(?P<chave_pos>[-\w\d]+)/aprovar/$',views.aprovar_possibilidade, name='aprovar_possibilidade'),

    url(r'^potencial/$', views.projeto_potencial, name='projeto_potencia'),

    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/dadosbasicos/$', views.projeto_potencial_dadosbasicos, name='projeto_potencial_dadosbasicos'),

    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/dadosfinanceiros/$', views.projeto_potencial_dadosfinanceiros, name='projeto_potencial_dadosfinanceiros'),

    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/nucleo/$', views.projeto_potencial_nucleo, name='projeto_potencial_nucleo'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/nucleo/confirmar/$', views.confirmar_potencial_nucleo, name='confirmar_potencial_nucleo'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/nucleo/delete/(?P<id_nucleo>[-\w\d]+)$', views.delete_potencial_nucleo, name='projeto_potencial_nucleo'),

    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/localizacao/$', views.projeto_potencial_localizacao, name='projeto_potencial_localizacao'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/localizacao/save/estado$',views.localizacao_potencial_save_estado, name='localizacao_potencial_save_estado'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/localizacao/save/regiao$',views.localizacao_potencial_save_regiao, name='localizacao_potencial_save_regiao'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/localizacao/save/municipio$',views.localizacao_potencial_save_municipio, name='localizacao_potencial_save_municipio'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/localizacao/save/pais$',views.localizacao_potencial_save_pais, name='localizacao_potencial_save_pais'),


    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/documentos/$', views.projeto_potencial_documentos, name='projeto_potencial_documentos'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/documentos/delete/(?P<id_documento>[-\w\d]+)$', views.delete_potencial_documentos, name='delete_potencial_documentos'),

    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/criar/integrante$', views.criar_integrante, name='criar_integrante'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/incluir/integrante$', views.incluir_integrante_equipe, name='incluir_integrante_equipe'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/excluir/(?P<id_integrante>[-\w\d]+)/integrante$', views.excluir_integrante_equipe, name='excluir_integrante_equipe'),

    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/parceiros/$', views.projeto_potencial_parceiros, name='projeto_potencial_parceiros'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/parceiros/delete/(?P<id_parceiro>[-\w\d]+)$', views.delete_potencial_parceiros, name='delete_potencial_parceiros'),
    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/cadastro_potencial/(?P<chave_potencial>[-\w\d]+)/finalizar/$',views.cadastro_finalizar_projeto_potencial, name='cadastro_finalizar_projeto_potencial'),

    url(r'^potencial/(?P<id_potencial>[-\w\d]+)/visualizar/(?P<chave_projeto>[-\w\d]+)/$',views.visualizar_projeto_potencial, name='visualizar_projeto_potencial'),

    url(r'^(?P<id_proj>[-\w\d]+)/dadosbasicos/addcontato/(?P<situacao_projeto>[-\w\d]+)$',views.cadastro_dados_basicos_contato, name='cadastro_dados_basicos_contato'),
    url(r'^(?P<id_proj>[-\w\d]+)/dadosbasicos/deletecontato/(?P<id_contato>[-\w\d]+)/(?P<situacao_projeto>[-\w\d]+)$',views.delete_dados_basicos_contato, name='delete_dados_basicos_contato'),

    url(r'^(?P<id_proj>[-\w\d]+)/dadosfinanceiros/addgastofinanceiro/(?P<fase_projeto>[-\w\d]+)$',views.cadastro_dados_financeiros_gasto, name='cadastro_dados_financeiros_gasto'),
    url(r'^(?P<id_proj>[-\w\d]+)/dadosfinanceiros/deletegastofinanceiro/(?P<id_gasto>[-\w\d]+)/(?P<fase_projeto>[-\w\d]+)$',views.delete_dados_financeiros_gasto, name='delete_dados_financeiros_gasto'),

    url(r'^(?P<id_proj>[-\w\d]+)/eliminar_projeto/(?P<fase_projeto>[-\w\d]+)$',views.eliminar_projeto, name='eliminar_projeto'),

    url(r'^eliminado/$', views.projeto_eliminado, name='eliminado'),

]