from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from appinicio.models import Auto
from appinicio.forms import CrearAutoFormulario, BuscarAuto, EditarAutoFormulario

fecha = datetime.now()

def inicio(request):
    return render(request, 'appinicio/index.html')

def aboutme(request):
    return render(request, 'appinicio/aboutme.html')

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

def crear_auto(request):
    
    print('Valor de la request: ' , request)
    print('Valor de GET: ' , request.GET)
    print('Valor de POST: ' , request.POST)
    
    if request.method == 'POST':
        formulario = CrearAutoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            auto = Auto(marca=datos.get('marca'),modelo=datos.get('modelo'))
            auto.save()
            return redirect('autos')
        
    formulario = CrearAutoFormulario(request.POST)
    return render(request, 'appinicio/creacion.html', {'formulario': formulario})


def autos(request):
    
    formulario = BuscarAuto(request.GET)
    if formulario.is_valid():
        marca = formulario.cleaned_data ['marca']
        
    autos = Auto.objects.filter(marca__icontains=marca)
    
    return render(request, 'appinicio/autos.html', {'autos': autos, 'formulario': formulario})


def eliminar_auto(request, id):
    auto = Auto.objects.get(id=id)
    auto.delete()
    return redirect('autos')

def editar_auto(request, id):
    auto = Auto.objects.get(id=id)
    
    formulario = EditarAutoFormulario(initial={'marca': auto.marca,'modelo': auto.modelo})
    
    if request.method == 'POST':
        formulario = EditarAutoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            auto.marca = info ['marca']
            auto.modelo = info ['modelo']
            
            auto.save()
            return redirect('autos')
    
    return render(request, 'appinicio/editar_auto.html', {'formulario':formulario, 'auto':auto})
    
def ver_auto(request, id):
    auto = Auto.objects.get(id=id)
    return render(request, 'appinicio/ver_auto.html', {'auto':auto})


#1.20