from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from users.forms import NuestroFormulario


def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
          username = formulario.cleaned_data.get('username')
          password = formulario.cleaned_data.get('password')
          
          user = authenticate(username=username, password=password)
          
          django_login(request, user)
          
          return redirect('inicio')
    
    return render(request, 'users/login.html', {'formulario': formulario})

def registro(request):
    
    formulario = NuestroFormulario()
    
    if request.method == 'POST':
        formulario = NuestroFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    return render(request, 'users/registro.html', {'formulario': formulario})