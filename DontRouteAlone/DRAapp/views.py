# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ruta, Usuario
# Create your views here.

def base(request):
	return render(request, "base.html", {})

class ListaRuta(ListView):
    model = Ruta
    context_object_name = "mis_rutas_favoritas"

class DetalleRuta(DetailView):

    model = Ruta

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetalleRuta, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lista_rutas'] = Ruta.objects.all()
        return context

class CreaUsuario(CreateView):
	model = Usuario
	fields = ['nombre', 'email', 'fNac', 'imagen']

class CreaRuta(CreateView):
	model = Ruta
	fields = ['titulo', 'descripcion', 'creador']

class ActualizaUsuario(UpdateView):
	model = Usuario
	fields = ['nombre', 'email', 'fNac', 'imagen']

class ActualizaRuta(CreateView):
	model = Ruta
	fields = ['titulo', 'descripcion', 'creador']

class BorraUsuario(DeleteView):
	model = Usuario

class BorraRuta(DeleteView):
	model = Ruta