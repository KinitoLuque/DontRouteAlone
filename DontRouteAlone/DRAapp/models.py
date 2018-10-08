# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=15)
	email = models.EmailField(max_length=254)
	fNac = models.DateField(auto_now=False, auto_now_add=False)
	imagen = models.ImageField()

	def __unicode__(self):
		return self.nombre

class Ruta(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    creador = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)

class Localizacion(models.Model):
	ruta = models.ForeignKey('Ruta', on_delete=models.CASCADE)
	orden = models.IntegerField()
	latitud = models.DecimalField(max_digits=9, decimal_places=6)
	longitud = models.DecimalField(max_digits=9, decimal_places=6)

class Participantes(models.Model):
	usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	ruta = models.ForeignKey('Ruta', on_delete=models.CASCADE)	