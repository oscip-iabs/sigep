# # -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
# from projeto.models import Projeto, localizacao_estado, localizacao_regiao, localizacao_municipio
from projeto.models import Projeto, Nucleo_x_Projeto


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
            'projeto_nucleo'		: forms.Select(attrs={'class': 'form-control border-input', 'required': True, 'multiple':'multiple'}),
		}

		fields = ('titulo',
                  'apoiador',
                  'tema_possibilidade',
                  'prazo_limite',
                  'descricao',
                  'periodo_execucao',
                  'check_possibilidade_cadastro_basico',)


class CadastroNucleoForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(CadastroNucleoForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Nucleo_x_Projeto
		widgets = {
			'nucleo' : forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
		}

		fields = ('projeto','nucleo',)


class CadastroDadosFinanceiroForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(CadastroDadosFinanceiroForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Projeto
		widgets = {
			'valor_estimado' : forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
		}

		fields = ('valor_estimado',
                  'check_possibilidade_cadastro_financeiro',)


class CadastroDadosLocalizacaoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroDadosLocalizacaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Projeto
        widgets = {
            'localizacao_mundial': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
            'localizacao_abrangencia': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
            'localizacao_descricao': forms.Textarea(attrs={'class': 'form-control border-input textarea', 'required': True}),
        }

        fields = ('localizacao_mundial',
                  'localizacao_descricao',
                  'localizacao_abrangencia',
                  'check_possibilidade_cadastro_localizacao',)


class FinalizarCadastroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FinalizarCadastroForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Projeto
        widgets = {
            'possibilidade_responsavel': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
        }

        fields = ('possibilidade_responsavel',
                  'status',)
