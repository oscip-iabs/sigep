# # -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
# from projeto.models import Projeto, localizacao_estado, localizacao_regiao, localizacao_municipio
from projeto.models import Projeto


class InformacoesBasicasProjeto(ModelForm):
	def __init__(self, *args, **kwargs):
		super(InformacoesBasicasProjeto, self).__init__(*args, **kwargs)

	class Meta:
		model = Projeto
		widgets = {
			'titulo'   : forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
			'apoiador' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
		}

		fields = ('titulo',
				  'apoiador',
				  'chave',
				  'status',)


class CadastroDadosBasicosForm(ModelForm):
	
	def __init__(self, *args, **kwargs):
		super(CadastroDadosBasicosForm, self).__init__(*args, **kwargs)
	
	class Meta:
		model = Projeto
		widgets = {
			'titulo'				: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
			'apoiador'				: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
			'periodo_execucao'		: forms.TextInput(attrs={'type':'number', 'class':'form-control border-input', 'required': True, 'step':'1',}),
			'prazo_limite'			: forms.TextInput(attrs={'type':'date'  , 'class':'form-control border-input', 'required': True, 'placeholder': 'dd/mm/aaaa'}),
			'tema_possibilidade'	: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
			'descricao'				: forms.Textarea(attrs={'class': 'form-control border-input', 'maxlength': 10000, 'required': True}),
            'fk_nucleo'             : forms.Select(attrs={'class': 'form-control border-input', 'required': True, 'multiple':'multiple'}),
		}

		fields = ('titulo',
                  'apoiador',
                  'status',
                  'tema_possibilidade',
                  'prazo_limite',
                  'descricao',
                  'periodo_execucao',
                  'check_possibilidade_cadastro_basico',
                  'fk_nucleo',)



# class localizacaoRegialNacional(ModelForm):
# 	class Meta:
# 		model = Projeto
# 		widgets = {
# 			'localizacao_area_nac' : forms.Select(attrs={'class':'form-control border-input', 'required': True}),
# 		}

# 		fields = ('status_projeto',
# 			'localizacao_area_nac',)


# class localizacaoEstado(ModelForm):
# 	class Meta:
# 		model = localizacao_estado
# 		widgets = {
# 			'nome_estado' : forms.Select(attrs={'class':'form-control border-input', 'required': True}),
# 		}

# 		fields = ('projeto',
# 			'nome_estado',)


# class localizacaoRegiao(ModelForm):
# 	class Meta:
# 		model = localizacao_regiao
# 		widgets = {
# 			'nome_regiao' : forms.Select(attrs={'class':'form-control border-input', 'required': True}),
# 		}

# 		fields = ('projeto',
# 			'nome_regiao',)


# class localizacaoMunicipio(ModelForm):
# 	class Meta:
# 		model = localizacao_municipio
# 		widgets = {
# 			'nome_municipio' : forms.Select(attrs={'class':'form-control border-input', 'required': True}),
# 		}

# 		fields = ('projeto',
# 			'nome_municipio',)

# class LocalPaisForm(ModelForm):
	
# 	class Meta:
# 		model = Projeto
# 		widgets = {
# 			'local_pais' : forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
# 		}

# 		fields = ('local_pais',)

