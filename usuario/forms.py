# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):

	User._meta.get_field('first_name').blank = False
	User._meta.get_field('last_name').blank = False
	User._meta.get_field('email').blank = False
	User._meta.get_field('username').blank = False
	User._meta.get_field('password').blank = False

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control border-input', 'maxlength':255, 'id':'primeiro-nome', 'placeholder':'Informe o primeiro nome do usuario'}),
			'last_name' : forms.TextInput(attrs={'class': 'form-control border-input', 'maxlength':255, 'id':'ultimo-nome', 'placeholder':'Informe o ultimo nome do usuario'}),
			'email'     : forms.TextInput(attrs={'class': 'form-control border-input', 'maxlength':255, 'id':'email', 'placeholder':'Informe o e-mail do usuario'}),
			'username'  : forms.TextInput(attrs={'class': 'form-control border-input', 'maxlength':255, 'id':'username', 'placeholder':'Informe o nome no usuario'}),
			'password'  : forms.PasswordInput(attrs={'class': 'form-control border-input', 'maxlength':255, 'id':'pwd', 'placeholder':'Informe a senha'}),
		}

	def save(self, commit=True):
		user = super(UserModelForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user


