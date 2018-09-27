# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
import datetime

from iabs_main.models import Geral_Status
from usuario.models import Usuario_Perfil, Notificacao_Usuario
from projeto.models import Projeto, Nucleo_x_Projeto, Historico_Projeto, Avaliacao_Possibilidade
from projeto.utils import generate_project_key

from projeto.forms import InformacoesBasicasProjeto, CadastroDadosBasicosForm, CadastroNucleoForm, \
    CadastroDadosFinanceiroForm, CadastroDadosLocalizacaoForm, FinalizarCadastroForm, AvaliacaoDadosDisabledForm, \
    AvaliacaoAdequacaoForm


from django.contrib.auth.models import Group
from django.contrib.auth.models import User



def is_admin(user):
    return user.groups.filter(name='iabs_admin').exists()

def request_user(request):
    return request.user.email


@login_required
@user_passes_test(is_admin)
def inicio_projeto(request):
    user_email = request_user(request)
    projetoObj = Projeto.objects.all()




    return render(request, 'projeto/home/home.html', locals())


# Metodo para iniciar o cadasto da possibilidade
# aqui faz o init dos dados na tabela projeto
@login_required
@user_passes_test(is_admin)
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

# Dados basicos referente ao basico da possibilidade possibilidade, cada metodo de cadastro
# das guias da possibilidade apos aprovados serao incrementado informacoes.
@login_required
@user_passes_test(is_admin)
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

# Dados bancarios iniciais da possibilidade
# guia de cadastro inicial da possibilidade
@login_required
@user_passes_test(is_admin)
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

# Nucleo da possibilidade, as possibilidades podem ter um ou mais nucleos
# guia de cadastro inicial da possibilidade
@login_required
@user_passes_test(is_admin)
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

# Informações referente a localizacao e area de atuacao
# guia de cadastro inicial da possibilidade
@login_required
@user_passes_test(is_admin)
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

# metodo para finalizar e definir responsavel pela possibilidade
@login_required
@user_passes_test(is_admin)
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

            notify_user = Notificacao_Usuario(
                date_created=now,
                titulo='Possibilidade %s na sua responsabilidade' % (chave_pos),
                descricao='Você foi definido como responsável da possibilidade %s' % (chave_pos),
                tipo='RESPONSAVEL_POSSIBILIDADE',
                visualizada=False,
                referencia=id_pos
            )
            notify_user.save()

            print 'teste'

            return redirect('/projeto/')

    return render(request, 'projeto/cadastro_possibilidade/cadastro_comp_dados_localizacao.html', locals(), )


@login_required
@user_passes_test(is_admin)
def avaliar_possibilidade(request, id_pos, chave_pos):

    possibilidade = Projeto.objects.get(id=id_pos, chave=chave_pos)
    usuario = Usuario_Perfil.objects.get(email=request.user.email)

    # possibilidade.possibilidade_responsavel.email == usuario.email

    adequacoes_basico = Avaliacao_Possibilidade.objects.filter(projeto=possibilidade, categoria=0)
    adequacoes_financeiro = Avaliacao_Possibilidade.objects.filter(projeto=possibilidade, categoria=1)
    adequacoes_nucleo = Avaliacao_Possibilidade.objects.filter(projeto=possibilidade, categoria=2)
    adequacoes_area = Avaliacao_Possibilidade.objects.filter(projeto=possibilidade, categoria=3)

    avaliacaoDadosForm = AvaliacaoDadosDisabledForm(request.POST or None, instance=possibilidade)

    novaAdequacao = AvaliacaoAdequacaoForm(request.POST or None)

    if request.method == 'POST':
        if novaAdequacao.is_valid():
            categoria = int(request.POST['categoria_adequacao'])

            adequacao_obj = novaAdequacao.save(commit=False)
            adequacao_obj.categoria = categoria
            adequacao_obj.projeto = possibilidade
            adequacao_obj.user_avaliador = usuario
            adequacao_obj.save()

            now = datetime.datetime.now()
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro de adequação na possibilidade ' + possibilidade.chave,
                tipo='AVALIACAO_ADEQUACAO_POSSIBILIDADE',
                projeto=possibilidade,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/%s/possibilidade/%s/avaliar' % (id_pos, chave_pos))


    return render(request, 'projeto/avaliacao_possibilidade/avaliacao_inicial.html', locals(), )


@login_required
@user_passes_test(is_admin)
def aprovar_possibilidade(request, id_pos, chave_pos):

    possibilidade = Projeto.objects.get(id=id_pos, chave=chave_pos)
    usuario = Usuario_Perfil.objects.get(email=request.user.email)

    print 'possibilidade'


    #
    # if possibilidade.possibilidade_responsavel.email == usuario.email:
    #     print 'Usuario responsavel pela possibilidade'
    # else:
    #     print 'USUARIO NEGADO'

    return redirect('/projeto')


    # return render(request, 'projeto/avaliacao_possibilidade/avaliacao_inicial.html', locals(), )