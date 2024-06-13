from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from appinicio.models import Auto

fecha = datetime.now()

def inicio(request):
    # return HttpResponse ('Bienvenidos a mi inico')
    return render(request, 'appinicio/index.html')

def template1(request, nombre, apellido):
    return HttpResponse(f'<h1>Mi Template 1</h1> -- Fecha: {fecha} -- Buenas {nombre} {apellido}')

def template2 (request, nombre, apellido):
       
    template = loader.get_template('template2.html')
    
    datos = {
        'fecha': fecha,
        'nombre': nombre ,
        'apellido': apellido ,
    }

    return render (request, 'template2.html',datos)

def crear_auto(request, marca, modelo):
    auto = Auto(marca=marca, modelo=modelo)
    auto.save()
    return render(request, 'auto_templates/creacion.html', {"auto": auto})