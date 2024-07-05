from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Paleta

class Paletas(ListView):
    model = Paleta
    template_name = 'paletas/listado_de_paletas.html'
    context_object_name = 'paletas'
    
class CrearPaleta(CreateView):
    model = Paleta
    template_name = 'paletas/crear_paleta.html'
    success_url = ''
    fields = ['marca','descripcion','fecha']
    
class EditarPaleta(UpdateView):
    ...