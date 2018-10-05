# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Usuario
from .models import Ruta
from .models import Localizacion
from .models import Participantes

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ruta)
admin.site.register(Localizacion)
admin.site.register(Participantes)