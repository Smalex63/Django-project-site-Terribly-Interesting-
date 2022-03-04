from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Stories, Comment


class ContactForm(forms.Form):
	subject = forms.CharField(label='Тема', widget = forms.TextInput(attrs={
		'class': 'form-control'}))
	content = forms.CharField(label='Текст', widget = forms.Textarea(attrs={
		'class': 'form-control', 'rows': 5}))


class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label='Имя пользователя', widget =
	forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='Пароль', widget = forms.PasswordInput(
		attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
	username = forms.CharField(label='Имя пользователя', widget =
	forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label='Пароль', widget = forms.PasswordInput(
		attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='Подтверждение пароля', widget =
	forms.PasswordInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='E-mail', widget = forms.EmailInput(
		attrs={'class': 'form-control'}))
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
	

class StoryForm(forms.ModelForm):
	class Meta:
		model = Stories
		fields = ('title', 'text', 'category')
		widgets = {
		    'title': forms.TextInput(attrs={'class': 'form-control'}),
		    'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
		    'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('content',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
		self.fields['content'].widget = Textarea(attrs={'rows': 5})


