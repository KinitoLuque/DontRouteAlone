# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CreaUsuario, ActualizaUsuario

from .models import Usuario
from .models import Ruta
from .models import Localizacion
from .models import Participantes

# Register your models here.

class UsuarioAdministrador(UserAdmin):
	add_form = CreaUsuario
	form = ActualizaUsuario
	model = Usuario
	list_display = ['email', 'username', 'fNac', 'imagen']

admin.site.register(Usuario, UsuarioAdministrador)
admin.site.register(Ruta)
admin.site.register(Localizacion)
admin.site.register(Participantes)