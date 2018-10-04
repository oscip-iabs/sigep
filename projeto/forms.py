# # -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from projeto.models import Projeto, Nucleo_x_Projeto, Avaliacao_Possibilidade, Documento, Contato, Parceiro, \
    Estado_x_Projeto, Regiao_x_Projeto, Municipio_x_Projeto, Pais_x_Projeto


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
            'titulo_abreviado'		: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
            'origem_projeto'		: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
            'apoiador'				: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
            'periodo_execucao'		: forms.TextInput(attrs={'type':'number', 'class':'form-control border-input', 'required': True, 'step':'1',}),
            'prazo_limite'			: forms.TextInput(attrs={'type':'date'  , 'class':'form-control border-input', 'required': True, 'placeholder': 'dd/mm/aaaa'}),
            'tema_possibilidade'	: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
            'descricao'				: forms.Textarea(attrs={'class': 'form-control border-input', 'maxlength': 10000, 'required': True}),
            'projeto_nucleo'		: forms.Select(attrs={'class': 'form-control border-input', 'required': True, 'multiple':'multiple'}),
        }

        fields = ('titulo',
            'titulo_abreviado',
            'origem_projeto',
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
            'localizacao_descricao': forms.Textarea(attrs={'class': 'form-control border-input textarea', 'required': True}),
        }

        fields = ('localizacao_mundial',
                  'localizacao_descricao',
                  'check_possibilidade_cadastro_localizacao',)


class CadastroEstadoLocalizacaoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroEstadoLocalizacaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Estado_x_Projeto
        widgets = {
            'estado_projeto': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
        }

        fields = ('projeto',
                  'estado_projeto',)


class CadastroRegiaoLocalizacaoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroRegiaoLocalizacaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Regiao_x_Projeto
        widgets = {
            'regiao_projeto': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
        }

        fields = ('projeto',
                  'regiao_projeto',)


class CadastroMunicipioLocalizacaoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroMunicipioLocalizacaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Municipio_x_Projeto
        widgets = {
            'municipio_projeto': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
        }

        fields = ('projeto',
                  'municipio_projeto',)


class CadastroInternacionalLocalizacaoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroInternacionalLocalizacaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Pais_x_Projeto
        widgets = {
            'pais_projeto': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
        }

        fields = ('projeto',
                  'pais_projeto',)


class FinalizarCadastroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FinalizarCadastroForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Projeto
        widgets = {
            'possibilidade_responsavel': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
            'prioridade_projeto': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
            'justificativa_prioridade': forms.Textarea(attrs={'class': 'form-control border-input', 'required': True}),
        }


        fields = ('possibilidade_responsavel',
                  'prioridade_projeto',
                  'justificativa_prioridade',
                  'status',)


class AvaliacaoDadosDisabledForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AvaliacaoDadosDisabledForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['titulo'].widget.attrs['readonly'] = True
            self.fields['apoiador'].widget.attrs['readonly'] = True
            self.fields['tema_possibilidade'].widget.attrs['readonly'] = True
            self.fields['prazo_limite'].widget.attrs['readonly'] = True
            self.fields['periodo_execucao'].widget.attrs['readonly'] = True
            self.fields['descricao'].widget.attrs['readonly'] = True
            self.fields['valor_estimado'].widget.attrs['readonly'] = True
            self.fields['localizacao_mundial'].widget.attrs['readonly'] = True
            self.fields['localizacao_abrangencia'].widget.attrs['readonly'] = True
            self.fields['localizacao_descricao'].widget.attrs['readonly'] = True

    class Meta:
        model = Projeto
        widgets = {
            'titulo'				: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
            'apoiador'				: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
            'periodo_execucao'		: forms.TextInput(attrs={'type':'number', 'class':'form-control border-input', 'required': True, 'step':'1',}),
            'prazo_limite'			: forms.TextInput(attrs={'type':'date'  , 'class':'form-control border-input', 'required': True, 'placeholder': 'dd/mm/aaaa'}),
            'tema_possibilidade'	: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
            'descricao'				: forms.Textarea(attrs={'class': 'form-control border-input', 'maxlength': 10000, 'required': True}),
            'valor_estimado'        : forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
            'localizacao_mundial'   : forms.Select(attrs={'class': 'form-control border-input', 'required': True, 'disabled': True}),
            'localizacao_descricao' : forms.Textarea(attrs={'class': 'form-control border-input textarea', 'required': True, 'disabled': True}),
        }

        fields = ('titulo',
            'apoiador',
            'tema_possibilidade',
            'prazo_limite',
            'descricao',
            'periodo_execucao',
            'valor_estimado',
            'localizacao_mundial',
            'localizacao_descricao',)


class AvaliacaoAdequacaoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AvaliacaoAdequacaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Avaliacao_Possibilidade
        widgets = {
            'adequacao': forms.Textarea(attrs={'class': 'form-control border-input area-recomendacao', 'required': True}),
        }

        fields = ('adequacao',
            'categoria',
            'projeto',
            'user_avaliador',)


class CadastroDadosBasicosPotencialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroDadosBasicosPotencialForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Projeto
        widgets = {
            'titulo'				: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
            'apoiador'				: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
            'periodo_execucao'		: forms.TextInput(attrs={'type':'number', 'class':'form-control border-input', 'required': True, 'step':'1',}),
            'prazo_limite'			: forms.TextInput(attrs={'type':'date'  , 'class':'form-control border-input', 'required': True, 'placeholder': 'dd/mm/aaaa'}),
            'previsao_resultado'	: forms.TextInput(attrs={'type':'date'  , 'class':'form-control border-input', 'placeholder': 'dd/mm/aaaa'}),
            'tema_possibilidade'	: forms.TextInput(attrs={'type':'text'  , 'class':'form-control border-input', 'required': True}),
            'descricao'				: forms.Textarea(attrs={'class': 'form-control border-input', 'maxlength': 10000, 'required': True}),
            'projeto_nucleo'		: forms.Select(attrs={'class': 'form-control border-input', 'required': True, 'multiple':'multiple'}),
            'tipo_contratacao'		: forms.Select(attrs={'class': 'form-control border-input', 'required': True, }),
        }

        fields = ('titulo',
            'apoiador',
            'tema_possibilidade',
            'prazo_limite',
            'descricao',
            'periodo_execucao',
            'previsao_resultado',
            'tipo_contratacao',
            'check_projeto_potencial_cadastro_basico',)


class formContato(ModelForm):
    def __init__(self, *args, **kwargs):
        super(formContato, self).__init__(*args, **kwargs)

    class Meta:
        model = Contato
        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
            'telefone': forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
            'email': forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
            'info_contato': forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
        }

        fields = ('nome',
            'telefone',
            'email',
            'info_contato',
            'projeto')


class CadastroDadosFinanceiroPotencialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroDadosFinanceiroPotencialForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Projeto
        widgets = {
            'valor_estimado': forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
        }

        fields = ('valor_estimado',
                  'check_possibilidade_cadastro_financeiro',)


class CadastroNucleoPotencialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroNucleoPotencialForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Nucleo_x_Projeto
        widgets = {
            'nucleo' : forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
        }

        fields = ('projeto', 'nucleo',)


class CadastroDadosLocalizacaoPotencialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroDadosLocalizacaoPotencialForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Projeto
        widgets = {
            'localizacao_mundial': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
            'localizacao_descricao': forms.Textarea(attrs={'class': 'form-control border-input textarea', 'required': True}),
        }

        fields = ('localizacao_mundial',
                  'localizacao_descricao',
                  'check_projeto_potencial_cadastro_localizacao',)


class CadastroDocumentoPotencialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroDocumentoPotencialForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Documento
        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
            'link': forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
        }

        fields = ('nome',
            'link',
            'projeto')


class CadastroParceiroPotencialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroParceiroPotencialForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Parceiro
        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
            'nome_responsavel': forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
            'telefone': forms.TextInput(attrs={'type': 'text', 'class': 'form-control border-input', 'required': True}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control border-input', 'required': True}),
            'formaliza_parceria': forms.RadioSelect(attrs={'name': 'radio1'}),
            'existe_instrumento_formal': forms.RadioSelect(attrs={'class': 'check-cronograma'}),
            'tipo_instrumento': forms.Select(attrs={'class': 'form-control border-input', 'required': True}),
        }

        fields = ('nome',
                  'nome_responsavel',
                  'telefone',
                  'email',
                  'projeto',
                  'formaliza_parceria',
                  'existe_instrumento_formal',
                  'tipo_instrumento',)
