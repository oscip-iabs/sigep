# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import datetime

from iabs_main.models import Geral_Status
from usuario.models import Usuario_Perfil
from projeto.models import Projeto, Nucleo_x_Projeto, Historico_Projeto
from projeto.utils import generate_project_key

from projeto.forms import InformacoesBasicasProjeto, CadastroDadosBasicosForm, CadastroNucleoForm, \
    CadastroDadosFinanceiroForm, CadastroDadosLocalizacaoForm, FinalizarCadastroForm




def inicio(request):
	projetoObj = Projeto.objects.all()

	return render(request, 'projeto/home/home.html', locals())


def add_possibilidade(request):
    formPossibilidade = InformacoesBasicasProjeto(request.POST or None)

    if request.method == 'POST':
        if formPossibilidade.is_valid():
            chave_projeto = 'PRO-'+str(generate_project_key())
            status_form = Geral_Status.objects.get(referencia='CADASTRO COMPLETO INICIADO', chave='CADASTRO_COMPLETO_INICIADO')

            projeto_obj = formPossibilidade.save(commit=False)
            projeto_obj.chave = chave_projeto
            projeto_obj.status = status_form
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao = now,
                texto = 'Inicio do cadastro de uma nova possibilidade',
                tipo = 'CADASTRO_POSSIBILIDADE',
                projeto = projeto_obj,
                modified_user = usuario
            )

            historicProject.save()

            return redirect('/projeto')

    return render(request, 'projeto/cadastro_possibilidade/possibilidade_inicio.html', locals(),)


def cadastro_dados_basicos_possibilidade(request, id_pos, chave_pos):
    TABS = 'BASICO'
    obj_projeto = Projeto.objects.get(id=id_pos, chave=chave_pos)
    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=obj_projeto)
    formPossibilidade = CadastroDadosBasicosForm(request.POST or None, instance=obj_projeto)

    if request.method == 'POST':
        if formPossibilidade.is_valid():
            projeto_obj = formPossibilidade.save(commit=False)
            projeto_obj.check_possibilidade_cadastro_basico = True
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro dos dados básicos da possibilidade '+obj_projeto.chave,
                tipo='CADASTRO_POSSIBILIDADE',
                projeto=obj_projeto,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/%s/cadastro/%s/dadosbasicos' % (id_pos, chave_pos))


    return render(request, 'projeto/cadastro_possibilidade/cadastro_comp_dados_basicos.html', locals(), )


def cadastro_dados_financeiros_possibilidade(request, id_pos, chave_pos):
    TABS = 'FINANCEIRO'
    obj_projeto = Projeto.objects.get(id=id_pos, chave=chave_pos)
    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=obj_projeto)
    formFinanceiro = CadastroDadosFinanceiroForm(request.POST or None, instance=obj_projeto)

    if request.method == 'POST':
        if formFinanceiro.is_valid():
            projeto_obj = formFinanceiro.save(commit=False)
            projeto_obj.check_possibilidade_cadastro_financeiro = True
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro das informações financeiras da possibilidade ' + obj_projeto.chave,
                tipo='CADASTRO_POSSIBILIDADE',
                projeto=obj_projeto,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/%s/cadastro/%s/dadosfinanceiros' % (id_pos, chave_pos))

    return render(request, 'projeto/cadastro_possibilidade/cadastro_comp_dados_financeiros.html', locals(), )


def cadastro_nucleo_possibilidade(request, id_pos, chave_pos):
    TABS = 'NUCLEO'
    obj_projeto = Projeto.objects.get(id=id_pos, chave=chave_pos)
    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=obj_projeto)

    try:
        nucleo_cadastrado = Nucleo_x_Projeto.objects.filter(projeto=obj_projeto)
    except:
        nucleo_empty = True

    formNucleo = CadastroNucleoForm(request.POST or None)

    if request.method == 'POST':
        if formNucleo.is_valid():
            projeto_obj = formNucleo.save(commit=False)
            projeto_check = Projeto.objects.filter(id=id_pos, chave=chave_pos).update(check_possibilidade_cadastro_nucleo=True)
            projeto_obj.projeto = obj_projeto
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro do(s) Núcleo(s) da possibilidade ' + obj_projeto.chave,
                tipo='CADASTRO_POSSIBILIDADE',
                projeto=obj_projeto,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/%s/cadastro/%s/nucleo' % (id_pos, chave_pos))

    return render(request, 'projeto/cadastro_possibilidade/cadastro_comp_dados_nucleo.html', locals(), )


def cadastro_localizacao_possibilidade(request, id_pos, chave_pos):
    TABS = 'LOCALIZACAO'
    obj_projeto = Projeto.objects.get(id=id_pos, chave=chave_pos)
    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=obj_projeto)
    formLocalizacao = CadastroDadosLocalizacaoForm(request.POST or None, instance=obj_projeto)

    if request.method == 'POST':
        if formLocalizacao.is_valid():
            localizacao_obj = formLocalizacao.save(commit=False)
            localizacao_obj.check_possibilidade_cadastro_localizacao = True
            localizacao_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro da localização da possibilidade ' + obj_projeto.chave,
                tipo='CADASTRO_POSSIBILIDADE',
                projeto=obj_projeto,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/%s/cadastro/%s/localizacao' % (id_pos, chave_pos))

    return render(request, 'projeto/cadastro_possibilidade/cadastro_comp_dados_localizacao.html', locals(), )


def cadastro_finalizar_possibilidade(request, id_pos, chave_pos):
    obj_projeto = Projeto.objects.get(id=id_pos, chave=chave_pos)

    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=obj_projeto)

    if request.method == 'POST':
        if formFinalizar.is_valid():
            finalizar_obj = formFinalizar.save(commit=False)
            statusConcluido = Geral_Status.objects.get(referencia='CADASTRO DA POSSIBILIDADE CONCLUIDO', chave='CADASTRO_POSSIBILIDADE_CONCLUIDO')
            finalizar_obj.status = statusConcluido
            finalizar_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro da possibilidade ' + obj_projeto.chave + ' foi finalizado',
                tipo='CADASTRO_POSSIBILIDADE',
                projeto=obj_projeto,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/')

    return render(request, 'projeto/cadastro_possibilidade/cadastro_comp_dados_localizacao.html', locals(), )