# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
import datetime

from iabs_main.models import Geral_Status
from usuario.models import Usuario_Perfil, Notificacao_Usuario
from projeto.models import Projeto, Nucleo_x_Projeto, Historico_Projeto, Avaliacao_Possibilidade, Documento, Contato, \
    Parceiro, Equipe_Projeto
from projeto.utils import generate_project_key

from projeto.forms import InformacoesBasicasProjeto, CadastroDadosBasicosForm, CadastroNucleoForm, \
    CadastroDadosFinanceiroForm, CadastroDadosLocalizacaoForm, FinalizarCadastroForm, AvaliacaoDadosDisabledForm, \
    AvaliacaoAdequacaoForm, CadastroDadosBasicosPotencialForm, CadastroDocumentoPotencialForm, formContato, \
    CadastroDadosFinanceiroPotencialForm, CadastroDadosLocalizacaoPotencialForm, CadastroNucleoPotencialForm, \
    CadastroParceiroPotencialForm


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
    possibilidade_andamento = Projeto.objects.filter(status__in=[101001000, 101002000])
    possibilidade_completa = Projeto.objects.filter(status=102001000)

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
    formContPossibilidade = formContato(request.POST or None)

    contatoPossibilidade = Contato.objects.filter(projeto=obj_projeto)

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


@login_required
@user_passes_test(is_admin)
def cadastro_dados_basicos_possibilidade_contato(request, id_pos, chave_pos):
    possibilidade_cadastro = Projeto.objects.get(id=int(id_pos))

    formContPossibilidade = formContato(request.POST or None)

    if request.method == 'POST':
        if formContPossibilidade.is_valid():

            projeto_obj = formContPossibilidade.save(commit=False)
            projeto_obj.projeto = possibilidade_cadastro
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro de um novo contato nos dados basicos',
                tipo='CADASTRO_POSSIBILIDADE',
                projeto=projeto_obj.projeto,
                modified_user=usuario
            )
            historicProject.save()

    return redirect('/projeto/%s/cadastro/%s/dadosbasicos' % (id_pos, chave_pos))


@login_required
@user_passes_test(is_admin)
def cadastro_dados_basicos_possibilidade_del_contato(request, id_pos, chave_pos, id_contato):
    contato = Contato.objects.get(id=int(id_contato))

    try:
        contato.delete()

        now = datetime.datetime.now()
        usuario = Usuario_Perfil.objects.get(email=request.user.email)
        historicProject = Historico_Projeto(
            date_modificacao=now,
            texto='Exclusão de Documento ' + contato.projeto.chave,
            tipo='CADASTRO_POSSIBILIDADE',
            projeto=contato.projeto,
            modified_user=usuario
        )
        historicProject.save()
    except:
        print('Ops')

    return redirect('/projeto/%s/cadastro/%s/dadosbasicos' % (id_pos, chave_pos))


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

    if not nucleo_cadastrado:
        obj_projeto.check_possibilidade_cadastro_nucleo = False
        obj_projeto.save()

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


@login_required
@user_passes_test(is_admin)
def delete_possibilidade_nucleo(request, id_pos, chave_pos, id_nucleo):
    possibilidade_nucleo = Nucleo_x_Projeto.objects.get(id=int(id_nucleo))

    try:
        possibilidade_nucleo.delete()

        now = datetime.datetime.now()
        usuario = Usuario_Perfil.objects.get(email=request.user.email)
        historicProject = Historico_Projeto(
            date_modificacao=now,
            texto='Exclusão de Núcleo da possibilidade ' + chave_pos,
            tipo='CADASTRO_PROJETO_POTENCIAL',
            projeto=possibilidade_nucleo.projeto,
            modified_user=usuario
        )
        historicProject.save()
    except:
        print('Ops')

    return redirect('/projeto/%s/cadastro/%s/nucleo' % (id_pos, chave_pos))


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
                referencia=int(id_pos)
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
    status_aprovado = Geral_Status.objects.get(chave='CADASTRO_POSSIBILIDADE_APROVADO' , referencia='POSSIBILIDADE APROVADA')
    possibilidade = Projeto.objects.get(id=id_pos, chave=chave_pos)
    usuario = Usuario_Perfil.objects.get(email=request.user.email)

    if possibilidade.possibilidade_responsavel.email == usuario.email:
        Projeto.objects.filter(id=possibilidade.id).update(status=status_aprovado)
    else:
        print 'USUARIO NEGADO'

    return redirect('/projeto/potencial')

@login_required
@user_passes_test(is_admin)
def projeto_potencial(request):
    potencial_novo = Projeto.objects.filter(status=20101000)

    return render(request, 'projeto/potencial/home/home.html', locals(),)


# Metodo para iniciar o cadasto do projeto potencial
@login_required
@user_passes_test(is_admin)
def projeto_potencial_dadosbasicos(request, id_potencial):
    TABS = 'BASICO'
    potencial_cadastro = Projeto.objects.get(id=int(id_potencial))

    formPotencial = CadastroDadosBasicosPotencialForm(request.POST or None, instance=potencial_cadastro)
    formContPotencial = formContato(request.POST or None)

    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=potencial_cadastro)

    contatoPotencial = Contato.objects.filter(projeto=potencial_cadastro)

    if request.method == 'POST':
        if formPotencial.is_valid():

            projeto_obj = formPotencial.save(commit=False)
            projeto_obj.check_projeto_potencial_cadastro_basico = True
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Inicio do cadastro de um novo potencial',
                tipo='CADASTRO_PROJETO_POTENCIAL',
                projeto=projeto_obj,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/potencial/%s/dadosbasicos' % id_potencial)

    return render(request, 'projeto/potencial/cadastros/dadosbasicos.html', locals(),)


@login_required
@user_passes_test(is_admin)
def projeto_potencial_contato_dadosbasicos(request, id_potencial):
    potencial_cadastro = Projeto.objects.get(id=int(id_potencial))

    formContPotencial = formContato(request.POST or None)

    if request.method == 'POST':
        if formContPotencial.is_valid():

            projeto_obj = formContPotencial.save(commit=False)
            projeto_obj.projeto = potencial_cadastro
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro de um novo contato nos dados basicos do potencial',
                tipo='CADASTRO_PROJETO_POTENCIAL',
                projeto=projeto_obj.projeto,
                modified_user=usuario
            )
            historicProject.save()

    return redirect('/projeto/potencial/%s/dadosbasicos' % id_potencial)


@login_required
@user_passes_test(is_admin)
def projeto_potencial_del_contato_dadosbasicos(request, id_potencial, id_contato):
    potencial_contato = Contato.objects.get(id=int(id_contato))

    try:
        potencial_contato.delete()

        now = datetime.datetime.now()
        usuario = Usuario_Perfil.objects.get(email=request.user.email)
        historicProject = Historico_Projeto(
            date_modificacao=now,
            texto='Exclusão de Documento do potencial ' + potencial_contato.projeto.chave,
            tipo='CADASTRO_PROJETO_POTENCIAL',
            projeto=potencial_contato.projeto,
            modified_user=usuario
        )
        historicProject.save()
    except:
        print('Ops')

    return redirect('/projeto/potencial/%s/dadosbasicos' % id_potencial)


@login_required
@user_passes_test(is_admin)
def projeto_potencial_dadosfinanceiros(request, id_potencial):
    TABS = 'FINANCEIRO'
    potencial_cadastro = Projeto.objects.get(id=int(id_potencial))

    formFinanceiro = CadastroDadosFinanceiroPotencialForm(request.POST or None, instance=potencial_cadastro)

    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=potencial_cadastro)

    if request.method == 'POST':
        if formFinanceiro.is_valid():
            projeto_obj = formFinanceiro.save(commit=False)
            projeto_obj.check_projeto_potencial_cadastro_financeiro = True
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro das informações financeiras da possibilidade ' + projeto_obj.chave,
                tipo='CADASTRO_PROJETO_POTENCIAL',
                projeto=projeto_obj,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/potencial/%s/dadosfinanceiros' % id_potencial)

    return render(request, 'projeto/potencial/cadastros/dadosfinanceiro.html', locals(),)


@login_required
@user_passes_test(is_admin)
def projeto_potencial_nucleo(request, id_potencial):
    TABS = 'NUCLEO'
    potencial_cadastro = Projeto.objects.get(id=int(id_potencial))
    check_nucleo = potencial_cadastro.check_projeto_potencial_cadastro_nucleo

    all_user = Usuario_Perfil.objects.all()
    equipe_nucleo = Equipe_Projeto.objects.filter(projeto=int(id_potencial))

    formNucleo = CadastroNucleoPotencialForm(request.POST or None)

    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=potencial_cadastro)

    try:
        nucleo_cadastrado = Nucleo_x_Projeto.objects.filter(projeto=potencial_cadastro)
    except:
        nucleo_empty = True

    if not nucleo_cadastrado:
        potencial_cadastro.check_projeto_potencial_cadastro_nucleo = False
        potencial_cadastro.save()

    if request.method == 'POST':
        if formNucleo.is_valid():
            projeto_obj = formNucleo.save(commit=False)
            projeto_check = Projeto.objects.filter(id=id_potencial).update(check_projeto_potencial_cadastro_nucleo=True)
            projeto_obj.projeto = potencial_cadastro
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro do(s) Núcleo(s) do projeto potencial ' + potencial_cadastro.chave,
                tipo='CADASTRO_PROJETO_POTENCIAL',
                projeto=potencial_cadastro,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/potencial/%s/nucleo' % id_potencial)

    return render(request, 'projeto/potencial/cadastros/nucleo.html', locals(),)


@login_required
@user_passes_test(is_admin)
def confirmar_potencial_nucleo(request, id_potencial):
    try:
        projeto_obj = Projeto.objects.get(id=id_potencial)
        projeto_obj.check_projeto_potencial_cadastro_nucleo = True
        projeto_obj.save()

        now = datetime.datetime.now()
        usuario = Usuario_Perfil.objects.get(email=request.user.email)
        historicProject = Historico_Projeto(
            date_modificacao=now,
            texto='Confirmação do(s) Núcleo(s) no projeto potencial ' + projeto_obj.chave,
            tipo='CADASTRO_PROJETO_POTENCIAL',
            projeto=projeto_obj,
            modified_user=usuario
        )
        historicProject.save()

    except:
        print("Ops!")

    return redirect('/projeto/potencial/%s/nucleo' % id_potencial)


@login_required
@user_passes_test(is_admin)
def delete_potencial_nucleo(request, id_potencial, id_nucleo):
    potencial_nucleo = Nucleo_x_Projeto.objects.get(id=int(id_nucleo))

    try:
        potencial_nucleo.delete()

        now = datetime.datetime.now()
        usuario = Usuario_Perfil.objects.get(email=request.user.email)
        historicProject = Historico_Projeto(
            date_modificacao=now,
            texto='Exclusão de Núcleo do potencial ' + potencial_nucleo.projeto.chave,
            tipo='CADASTRO_PROJETO_POTENCIAL',
            projeto=potencial_nucleo.projeto,
            modified_user=usuario
        )
        historicProject.save()
    except:
        print('Ops')

    return redirect('/projeto/potencial/%s/nucleo' % (id_potencial))


@login_required
@user_passes_test(is_admin)
def criar_integrante(request, id_potencial):

    if request.method == 'POST':
        try:
            novo_participante = Usuario_Perfil(
                nome=request.POST.get('nome'),
                cpf=request.POST.get('cpf'),
                email=request.POST.get('email'),
                telefone=request.POST.get('telefone'),
                idade=request.POST.get('idade'),
                sexo=request.POST.get('sexo'),
            )
            novo_participante.save()
        except:
            return redirect('/projeto/potencial/%s/nucleo/' % (id_potencial,))

    return redirect('/projeto/potencial/%s/nucleo/' % (id_potencial,))


@login_required
@user_passes_test(is_admin)
def incluir_integrante_equipe(request, id_potencial):

    if request.method == 'POST':
        try:
            user_id = request.POST.get('participante_equipe')
            participante_equipe = Usuario_Perfil.objects.get(id=int(user_id))
            projeto_potencial = Projeto.objects.get(id=int(id_potencial))

            incluir_participante = Equipe_Projeto(
                participante=participante_equipe,
                projeto=projeto_potencial,
                responsabilidade=request.POST.get('responsabilidade')
            )
            incluir_participante.save()
        except:
            return redirect('/projeto/potencial/%s/nucleo/' % (id_potencial,))

    return redirect('/projeto/potencial/%s/nucleo/' % (id_potencial,))


@login_required
@user_passes_test(is_admin)
def excluir_integrante_equipe(request, id_potencial, id_integrante):

    try:
        Equipe_Projeto.objects.filter(id=int(id_integrante)).delete()
    except:
        return redirect('/projeto/potencial/%s/nucleo/' % (id_potencial,))

    return redirect('/projeto/potencial/%s/nucleo/' % (id_potencial,))


@login_required
@user_passes_test(is_admin)
def projeto_potencial_localizacao(request, id_potencial):
    TABS = 'LOCALIZACAO'
    potencial_cadastro = Projeto.objects.get(id=int(id_potencial))

    formLocalizacao = CadastroDadosLocalizacaoPotencialForm(request.POST or None, instance=potencial_cadastro)

    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=potencial_cadastro)

    if request.method == 'POST':
        if formLocalizacao.is_valid():
            localizacao_obj = formLocalizacao.save(commit=False)
            localizacao_obj.check_projeto_potencial_cadastro_localizacao = True
            localizacao_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro da localização do projeto potencial ' + localizacao_obj.chave,
                tipo='CADASTRO_PROJETO_POTENCIAL',
                projeto=localizacao_obj,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/potencial/%s/localizacao' % id_potencial)

    return render(request, 'projeto/potencial/cadastros/localizacao.html', locals(),)


@login_required
@user_passes_test(is_admin)
def projeto_potencial_documentos(request, id_potencial):
    TABS = 'DOCUMENTOS'
    potencial_cadastro = Projeto.objects.get(id=int(id_potencial))

    formDoc = CadastroDocumentoPotencialForm(request.POST or None)

    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=potencial_cadastro)

    try:
        doc_cadastrado = Documento.objects.filter(projeto=potencial_cadastro)
    except:
        doc_empty = True

    doc_potencial_cadastro = Documento.objects.filter(projeto=potencial_cadastro)

    if not doc_potencial_cadastro:
        potencial_cadastro.check_projeto_potencial_cadastro_documento = False
        potencial_cadastro.save()

    if request.method == 'POST':
        if formDoc.is_valid():
            projeto_obj = formDoc.save(commit=False)
            projeto_check = Projeto.objects.filter(id=id_potencial).update(check_projeto_potencial_cadastro_documento=True)
            projeto_obj.projeto = potencial_cadastro
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro do(s) Documento(s) do potencial ' + potencial_cadastro.chave,
                tipo='CADASTRO_PROJETO_POTENCIAL',
                projeto=potencial_cadastro,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/potencial/%s/documentos' % (id_potencial))

    return render(request, 'projeto/potencial/cadastros/documentos.html', locals(),)


@login_required
@user_passes_test(is_admin)
def delete_potencial_documentos(request, id_potencial, id_documento):
    potencial_documento = Documento.objects.get(id=int(id_documento))

    try:
        potencial_documento.delete()

        now = datetime.datetime.now()
        usuario = Usuario_Perfil.objects.get(email=request.user.email)
        historicProject = Historico_Projeto(
            date_modificacao=now,
            texto='Exclusão de Documento do potencial ' + potencial_documento.projeto.chave,
            tipo='CADASTRO_PROJETO_POTENCIAL',
            projeto=potencial_documento.projeto,
            modified_user=usuario
        )
        historicProject.save()
    except:
        print('Ops')

    return redirect('/projeto/potencial/%s/documentos' % id_potencial)


@login_required
@user_passes_test(is_admin)
def projeto_potencial_parceiros(request, id_potencial):
    TABS = 'PARCEIROS'
    potencial_cadastro = Projeto.objects.get(id=int(id_potencial))
    check_parceiro = potencial_cadastro.check_projeto_potencial_cadastro_parceiro

    formParceiro = CadastroParceiroPotencialForm(request.POST or None)

    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=potencial_cadastro)

    try:
        parceiro_cadastrado = Parceiro.objects.filter(projeto=potencial_cadastro)
    except:
        parceiro_empty = True

    if not parceiro_cadastrado:
        potencial_cadastro.check_projeto_potencial_cadastro_parceiro = False
        potencial_cadastro.save()

    if request.method == 'POST':
        if formParceiro.is_valid():
            projeto_obj = formParceiro.save(commit=False)
            projeto_check = Projeto.objects.filter(id=id_potencial).update(check_projeto_potencial_cadastro_parceiro=True)
            projeto_obj.projeto = potencial_cadastro
            projeto_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro de Parceiro(s) do projeto potencial ' + potencial_cadastro.chave,
                tipo='CADASTRO_PROJETO_POTENCIAL',
                projeto=potencial_cadastro,
                modified_user=usuario
            )
            historicProject.save()

            return redirect('/projeto/potencial/%s/parceiros' % id_potencial)

    return render(request, 'projeto/potencial/cadastros/parceiros.html', locals(),)


@login_required
@user_passes_test(is_admin)
def delete_potencial_parceiros(request, id_potencial, id_parceiro):
    potencial_parceiro = Parceiro.objects.get(id=int(id_parceiro))

    try:
        potencial_parceiro.delete()

        now = datetime.datetime.now()
        usuario = Usuario_Perfil.objects.get(email=request.user.email)
        historicProject = Historico_Projeto(
            date_modificacao=now,
            texto='Exclusão de Parceiro do potencial ' + potencial_parceiro.projeto.chave,
            tipo='CADASTRO_PROJETO_POTENCIAL',
            projeto=potencial_parceiro.projeto,
            modified_user=usuario
        )
        historicProject.save()
    except:
        print('Ops')

    return redirect('/projeto/potencial/%s/parceiros' % id_potencial)


# metodo para finalizar e definir responsavel pelo projeto potencial
@login_required
@user_passes_test(is_admin)
def cadastro_finalizar_projeto_potencial(request, id_potencial, chave_potencial):
    obj_projeto = Projeto.objects.get(id=id_potencial, chave=chave_potencial)

    formFinalizar = FinalizarCadastroForm(request.POST or None, instance=obj_projeto)

    if request.method == 'POST':
        if formFinalizar.is_valid():
            finalizar_obj = formFinalizar.save(commit=False)
            statusConcluido = Geral_Status.objects.get(referencia='CADASTRO PROJETO POTENCIAL COMPLETO', chave='CADASTRO_PROJETO_POTENCIAL_CONCLUIDO')
            finalizar_obj.status = statusConcluido
            finalizar_obj.save()

            now = datetime.datetime.now()
            usuario = Usuario_Perfil.objects.get(email=request.user.email)
            historicProject = Historico_Projeto(
                date_modificacao=now,
                texto='Cadastro do projeto potencial ' + obj_projeto.chave + ' foi finalizado',
                tipo='CADASTRO_PROJETO_POTENCIAL',
                projeto=obj_projeto,
                modified_user=usuario
            )
            historicProject.save()

            notify_user = Notificacao_Usuario(
                date_created=now,
                titulo='Projeto potencial %s na sua responsabilidade' % (chave_potencial),
                descricao='Você foi definido como responsável da possibilidade %s' % (chave_potencial),
                tipo='RESPONSAVEL_POSSIBILIDADE',
                visualizada=False,
                referencia=int(id_potencial)
            )
            notify_user.save()

            print 'teste'

            return redirect('/projeto/')

    return render(request, 'projeto/potencial/parceiros.html', locals(), )



    return redirect('/projeto/potencial/%s/documentos' % (id_potencial))
