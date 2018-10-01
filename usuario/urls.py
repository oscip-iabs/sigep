from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.do_login, name='login'),
    url(r'^logout/$', views.do_logout, name='logout'),

    url(r'^$', views.inicio, name='inicio'),

    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^minhas_acoes/$', views.minhas_acoes, name='minhas_acoes'),

    url(r'^minhas_notificacoes/$', views.minhas_notificacoes, name='minhas_notificacoes'),
    url(r'^notify_view/(?P<id_notify>[-\w\d]+)$', views.visualizar_notificacao, name='visualizar_notificacao'),


]

