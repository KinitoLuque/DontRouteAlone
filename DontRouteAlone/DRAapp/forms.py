from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class CreaUsuario(UserCreationForm):

	class Meta(UserCreationForm):
		model = Usuario
		fields = ('username', 'email', 'fNac', 'imagen')

class ActualizaUsuario(UserChangeForm):

	class Meta:
		model = Usuario
		fields = ('username', 'email', 'fNac', 'imagen')