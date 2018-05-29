# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render, redirect

from iabs_main.models import Geral_Status

from projeto.models import Projeto
from projeto.forms import InformacoesBasicasProjeto, CadastroDadosBasicosForm
from projeto.utils import generate_project_key


def inicio(request):
	projetoObj = Projeto.objects.all()
	
	return render(request, 'projeto/home/home.html', locals())


def add_possibilidade(request):
    formPossibilidade = InformacoesBasicasProjeto(request.POST or None)

    if request.method == 'POST':
        if formPossibilidade.is_valid():
            chave_projeto = 'PRO-'+str(generate_project_key())
            status_form = Geral_Status.objects.get(referencia='CADASTRO INICIAL DA POSSIBILIDADE', chave='CADASTRO_BASICO_NOVO')
                
            projeto_obj = formPossibilidade.save(commit=False)
            projeto_obj.chave = chave_projeto
            projeto_obj.status = status_form

            projeto_obj.save()
            return redirect('/projeto')

    return render(request, 'projeto/cadastro_possibilidade/possibilidade_inicio.html', locals(),)


def cadastro_dados_basicos_possibilidade(request, id_pos, chave_pos):
    obj_projeto = Projeto.objects.get(id=id_pos, chave=chave_pos)
    formPossibilidade = CadastroDadosBasicosForm(request.POST or None, instance=obj_projeto)

    if request.method == 'POST':
        print 'cadastro basico'

    return render(request, 'projeto/cadastro_possibilidade/cadastro_comp_dados_basicos.html', locals(), )

def cadastro_dados_financeiros_possibilidade(request, id_pos, chave_pos):
    obj_projeto = Projeto.objects.get(id=id_pos, chave=chave_pos)
    return render(request, 'projeto/cadastro_possibilidade/cadastro_comp_dados_financeiros.html', locals(), )

def cadastro_dados_financiador_possibilidade(request, id_pos, chave_pos):
    obj_projeto = Projeto.objects.get(id=id_pos, chave=chave_pos)
    return render(request, 'projeto/cadastro_possibilidade/cadastro_comp_dados_financiador.html', locals(), )

# def cadastro_localizacao(request, chave):

# 	projetoObj = Projeto.objects.get(chave_projeto=chave)

# 	if projetoObj.localizacao_mundial == 0:
# 		localCadastro = 'nac'
# 		formLocalRegiao = localizacaoRegialNacional(request.POST or None, instance=projetoObj)
# 		if request.method == 'POST':
# 			if formLocalRegiao.is_valid():
# 				formRegiao = formLocalRegiao.save(commit=False)
# 				formRegiao.status_projeto = 100011001
# 				formRegiao.save()

# 				return redirect('/projeto/%s/%s'%(chave, formRegiao.localizacao_area_nac))

# 	if projetoObj.localizacao_mundial == 1:
# 		localCadastro = 'inter'
# 		formLocalPais = LocalPaisForm(request.POST or None, instance=projetoObj)
# 		if request.method == 'POST':
# 			if formLocalPais.is_valid():
# 				formPais = formLocalPais.save(commit=False)
# 				formPais.status_projeto = 100012000
# 				formPais.save()

# 				return redirect('/projeto/')		


# 	return render(request, 'projeto/localizacao-regiao.html', locals(),)


# def regiao_possibilidade(request, chave, regiao):

# 	projetoObj = Projeto.objects.get(chave_projeto=chave)	
# 	# import pdb; pdb.set_trace()
# 	if int(regiao) == 1:
# 		cadastroForm = 'Regional'
# 		formLocalRegiao = localizacaoRegiao(request.POST or None, instance=projetoObj)
		
# 		if request.method == 'POST':
# 			if formLocalRegiao.is_valid():
# 				acaoCadastro = request.POST['cadastro']
# 				estado = request.POST['nome_regiao']
# 				localizacao_regiao.objects.create(projeto=projetoObj, nome_regiao=estado)

# 				if acaoCadastro == 'cadastro_finalizar':
# 					return redirect('/projeto/')
# 				if acaoCadastro == 'cadastro_novo':
# 					return redirect('/projeto/%s/%s'%(chave, regiao))

# 	if int(regiao) == 2:
# 		cadastroForm = 'Estadual'
# 		formLocalEstado = localizacaoEstado(request.POST or None, instance=projetoObj)
		
# 		if request.method == 'POST':
# 			if formLocalEstado.is_valid():
# 				acaoCadastro = request.POST['cadastro']
# 				regiao = request.POST['nome_estado']
# 				localizacao_estado.objects.create(projeto=projetoObj, nome_estado=regiao)

# 				if acaoCadastro == 'cadastro_finalizar':
# 					return redirect('/projeto/')
# 				if acaoCadastro == 'cadastro_novo':
# 					return redirect('/projeto/%s/%s'%(chave, regiao))

# 	if int(regiao) == 3:
# 		cadastroForm = 'Municipal'
# 		formLocalMunicipio = localizacaoMunicipio(request.POST or None, instance=projetoObj)
		
# 		if request.method == 'POST':
# 			if formLocalMunicipio.is_valid():
# 				acaoCadastro = request.POST['cadastro']
# 				estado = request.POST['nome_municipio']
# 				localizacao_municipio.objects.create(projeto=projetoObj, nome_municipio=estado)

# 				if acaoCadastro == 'cadastro_finalizar':
# 					return redirect('/projeto/')
# 				if acaoCadastro == 'cadastro_novo':
# 					return redirect('/projeto/%s/%s'%(chave, regiao))

# 	return render(request, 'projeto/local-regional.html', locals(),)


# def avaliacao_possibilidade(request, chave):	

# 	projetoObj = Projeto.objects.get(id=chave)
# 	municipioObj = localizacao_municipio.objects.filter(projeto=projetoObj)	
# 	estadoObj = localizacao_estado.objects.filter(projeto=projetoObj)	
# 	regiaoObj = localizacao_regiao.objects.filter(projeto=projetoObj)	

# 	return render(request, 'projeto/avaliacao-projeto.html', locals(),)