from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from users.forms import NuestroFormulario, EditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from users.models import DatosExtra
from django.core.files.uploadedfile import InMemoryUploadedFile


def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
          username = formulario.cleaned_data.get('username')
          password = formulario.cleaned_data.get('password')
          
          user = authenticate(username=username, password=password)
          
          django_login(request, user)
          
          DatosExtra.objects.get_or_create()
          
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


@login_required
def editar_perfil(request):
    
    datosextra, created = DatosExtra.objects.get_or_create(user=request.user)
    formulario = EditarPerfil(initial={'avatar': datosextra.avatar}, instance=request.user)
    
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES ,instance=request.user)
        if formulario.is_valid():
            if 'avatar' in request.FILES:
                avatar = request.FILES['avatar']
                datosextra.avatar = avatar
            
            datosextra.save()
            formulario.save()
            return redirect('editar_perfil')
    
    return render(request, 'users/editar_perfil.html',{'formulario': formulario})



class CambiarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/cambiar_pass.html'
    success_url = reverse_lazy('editar_perfil')
    

@login_required
def ver_perfil(request):
    datosextra, created = DatosExtra.objects.get_or_create(user=request.user)
    user = request.user
    context = {
        'user': user,

    }
    return render(request, 'users/ver_perfil.html', context)
