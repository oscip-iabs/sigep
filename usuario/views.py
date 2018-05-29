# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pdb;
# pdb.set_trace()

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from usuario.forms import UserModelForm


def do_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		# import pdb; pdb.set_trace()
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

	# pdb.set_trace()
	all_users = User.objects.all()

	context = { 'all_users': all_users }

	return render(request, 'usuario/inicio.html', context)

@login_required
def cadastro(request):
	formUser = UserModelForm(request.POST or None)
	context = { 'form':formUser }

	if request.method == 'POST':
		if formUser.is_valid():
			formUser.save()
			return redirect('/usuario')

	return render(request, 'usuario/cadastro.html', context)