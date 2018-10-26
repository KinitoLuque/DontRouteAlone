# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

class Usuario(AbstractUser):
	email = models.EmailField(max_length=254)
	fNac = models.DateField(auto_now=False, auto_now_add=False, null=True)
	imagen = models.ImageField(blank=True)
	def __str__(self):
		return self.email
class Ruta(models.Model):
	titulo = models.CharField(max_length=30)
	descripcion = models.TextField()
	creador = models.ForeignKey('Usuario', on_delete=models.CASCADE, default=2)

class Localizacion(models.Model):
	ruta = models.ForeignKey('Ruta', on_delete=models.CASCADE)
	orden = models.IntegerField()
	latitud = models.DecimalField(max_digits=9, decimal_places=6)
	longitud = models.DecimalField(max_digits=9, decimal_places=6)

class Participantes(models.Model):
	usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	ruta = models.ForeignKey('Ruta', on_delete=models.CASCADE)