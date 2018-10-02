# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import Http404, HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from usuario.models import Usuario_Perfil, Notificacao_Usuario
from usuario.forms import UserModelForm

from projeto.models import Historico_Projeto, Projeto

import datetime

def do_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			login_error = False
			return redirect('/')
		else:
			login_error = True
			return render(request, 'usuario/login.html', context = { 'login_error':login_error })

	login_error = False

	return render(request, 'usuario/login.html', context = { 'login_error':login_error })


def do_logout(request):
    logout(request)
    return redirect('/usuario/login')


@login_required
def inicio(request):
    all_users = User.objects.all()
    context = { 'all_users': all_users }

    # Group.objects.get(id=request.user.grupo_id)

    return render(request, 'usuario/inicio.html', context)


@login_required
def cadastro(request):
    formUser = UserModelForm(request.POST or None)
    context = { 'form':formUser }

    if request.method == 'POST':
        if formUser.is_valid():
            fake_user = formUser.save(commit=False)
            fake_user.is_superuser = True
            fake_user.is_staff = True
            fake_user.is_active = True
            fake_user.save()
            now = datetime.datetime.now()
            perfil_user = Usuario_Perfil(
                date_created=now,
                nome=fake_user.first_name + ' ' + fake_user.last_name,
                email=fake_user.email,
                user_db=User.objects.get(id=fake_user.id)
            )
            perfil_user.save()

        return redirect('/usuario')

    return render(request, 'usuario/cadastro.html', context)


@login_required
def minhas_acoes(request):
    usuario = Usuario_Perfil.objects.get(email=request.user.email)
    myhistoric = Historico_Projeto.objects.filter(modified_user=usuario).order_by('-date_modificacao')
    context = {'myhistoric': myhistoric}
    return render(request, 'usuario/historico/minhas_acoes.html', context)


def minhas_notificacoes(request):
    if request.is_ajax():
        item_obj = []
        usuario = Usuario_Perfil.objects.get(email=request.user.email)
        notify = Notificacao_Usuario.objects.filter(modified_user=usuario.id, visualizada=False)
        item_obj.append(notify.count())
        for notificacao in notify:
            sub_item = []
            sub_item.append(notificacao.titulo)
            sub_item.append(notificacao.id)
            item_obj.append(sub_item)

        data = json.dumps(item_obj)
        return HttpResponse(data, content_type='application/json')

    else:
        raise Http404


@login_required
def visualizar_notificacao(request, id_notify):
    notify = Notificacao_Usuario.objects.get(id=id_notify)
    projeto_obj = Projeto.objects.get(id=notify.referencia)
    # Notificacao_Usuario.objects.filter(id=notify.id).update(visualizada=True)

    if projeto_obj.status.id == 102001000:
        return redirect('/projeto/%s/possibilidade/%s/avaliar/' % (projeto_obj.id, projeto_obj.chave))
    elif projeto_obj.status.id == 20201000:
        return redirect('/projeto/%s/possibilidade/%s/avaliar/' % (projeto_obj.id, projeto_obj.chave))

    return redirect('/')
