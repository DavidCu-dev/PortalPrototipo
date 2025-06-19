import os
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import formDatosUsuario
from .models import datosUsuarioM
# Create your views here.


def disclaimer(request):
    return render(request, 'disclaimer.html')


@login_required(login_url='iniciarSesion')
def home(request):
    datos = datosUsuarioM.objects.filter(user=request.user).first()
    return render(request, 'home.html', {
        'datosUsuario': datos
    })


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


def actualizarDatosUsuario(request):
    if request.method == 'GET':
        actualizacion = get_object_or_404(datosUsuarioM, user=request.user)
        form = formDatosUsuario(instance=actualizacion)
        return render(request, 'editDatUs.html', {
            'form': form
        })
    else:
        try:
            actualizacion = get_object_or_404(datosUsuarioM, user=request.user)
            form = formDatosUsuario(request.POST, instance=actualizacion)
            form.save()
            messages.success(request, 'Datos actualizados correctamente')
            return redirect('home')
        except ValueError:
            return render(request, 'editDatUs.html', {
                'form': form,
                'error': 'Error al actualizar los datos'
            })

def declaratoriaPropiedad(request):
        return render(request, 'Documentos/declaratoriaPropiedad.html')