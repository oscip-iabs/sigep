# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import user_passes_test, login_required


def is_admin(user):
    return user.groups.filter(name='iabs_admin').exists()


def request_user(request):
    return request.user.email


@login_required
@user_passes_test(is_admin)
def inicio_modelo(request):

    return render(request, 'modelo/home/home.html', locals())
