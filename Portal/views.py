import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import formDatosUsuario
# Create your views here.

def disclaimer(request):
    return render(request, 'disclaimer.html')


def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })
    
def cerrarSesion(request):
    logout(request)
    return redirect('home')


def iniciarSesion(request):
    
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],  password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')

def datosUsuario(request):
    if request.method == 'GET':
        return render(request, 'datosUsuario.html', {
            'form': formDatosUsuario
        })
    else:
        form = formDatosUsuario(request.POST)
        nuevosDatos = form.save(commit=False)
        nuevosDatos.user = request.user
        nuevosDatos.save()
        return redirect('home')