import os
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# impórtacion de models y forms
from .forms import formDatosUsuario, formDeclaratoriaPropiedad, formDeclaratoriaCumplimientoAmbiental, formCartaNotificacion, formReporteVisitaTecnica
from .models import datosUsuarioM, declaratoriaPropiedadModel, declaCumpliAmbModel, cartaNotificacionModel, reporteVisitaTecnicaModel

# generacion de documentos
from io import BytesIO
from docxtpl import DocxTemplate



def politicaPrivacidad(request):
    return render(request, 'PV.html')


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
                return redirect('datosUsuario')
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
                'error': 'Error al actualizar los datos, por favor intente de nuevo.'
            })

# formularios 

def declaratoriaPropiedad(request):
    # Buscar si ya existen datos para este usuario
    datos = declaratoriaPropiedadModel.objects.filter(user=request.user).first()

    # si se envia un formulario
    if request.method == 'POST':

        # si existen datos:
        if datos:
            # actualiza el registro existente (instance=datos) arriba
            form = formDeclaratoriaPropiedad(request.POST, instance=datos) 

        # Si no existen datos, crea uno nuevo
        else:
            form = formDeclaratoriaPropiedad(request.POST)

        # compruieba si el formulario cumple con las validaciones    
        if form.is_valid():
            # si es valido, guarda los datos
            instancia = form.save(commit=False)
            instancia.user = request.user  # Asegúrate de asignar el usuario si es necesario
            instancia.save()
            messages.success(request, 'Datos de Declaratoria de propiedad enviados correctamente')
            return redirect('home')
        else:
            messages.error(request, 'Por favor introdusca valores validos.')
            print(form.errors)
        
    # si no exsiosten datos:
    else:
        # Si ya existen datos, muestra el formulario con los datos
        if datos:
            form = formDeclaratoriaPropiedad(instance=datos)
        else:
            form = formDeclaratoriaPropiedad()

    return render(request, 'Documentos/declaratoriaPropiedad.html', {
        'form': form
    })

def declaratoriaCumplimientoAmbiental(request):
    # Buscar si ya existen datos para este usuario
    datos = declaCumpliAmbModel.objects.filter(user=request.user).first()

    # si se envia un formulario
    if request.method == 'POST':

        # si existen datos:
        if datos:
            # actualiza el registro existente (instance=datos) arriba
            form = formDeclaratoriaCumplimientoAmbiental(request.POST, instance=datos) 

        # Si no existen datos, crea uno nuevo
        else:
            form = formDeclaratoriaCumplimientoAmbiental(request.POST)

        # compruieba si el formulario cumple con las validaciones    
        
        if form.is_valid():
            # si es valido, guarda los datos
            print(request.POST)
            instancia = form.save(commit=False)
            instancia.user = request.user  # Asegúrate de asignar el usuario si es necesario
            instancia.save()
            messages.success(request, 'Datos de Declaratoria de Cumplimiento Ambiental enviados correctamente')
            return redirect('home')
        else:
            messages.error(request, 'Por favor introdusca valores validos.')
            print(form.errors)
    # si no exsiosten datos:
    else:
        # Si ya existen datos, muestra el formulario con los datos
        if datos:
            form = formDeclaratoriaCumplimientoAmbiental(instance=datos)
        else:
            form = formDeclaratoriaCumplimientoAmbiental()

    return render(request, 'Documentos/declaratoriaCA.html', {
        'form': form
    })


def cartaNotificacion(request):
    # Buscar si ya existen datos para este usuario
    datos = cartaNotificacionModel.objects.filter(user=request.user).first()

    # si se envia un formulario
    if request.method == 'POST':

        # si existen datos:
        if datos:
            # actualiza el registro existente (instance=datos) arriba
            form = formCartaNotificacion(request.POST, instance=datos) 

        # Si no existen datos, crea uno nuevo
        else:
            form = formCartaNotificacion(request.POST)

        # compruieba si el formulario cumple con las validaciones    
        
        if form.is_valid():
            # si es valido, guarda los datos
            print(request.POST)
            instancia = form.save(commit=False)
            instancia.user = request.user  # Asegúrate de asignar el usuario si es necesario
            instancia.save()
            messages.success(request, 'Datos de Carta de Notificacion enviados correctamente')
            return redirect('home')
        else:
            messages.error(request, 'Por favor introdusca valores validos.')
            print(form.errors) 
    # si no exsiosten datos:
    else:
        # Si ya existen datos, muestra el formulario con los datos
        if datos:
            form = formCartaNotificacion(instance=datos)
        else:
            form = formCartaNotificacion()

    return render(request, 'Documentos/cartaNotidicacion.html', {
        'form': form,
        'datos': datos
    })

def reporteVisitaTecnica(request):
    # Buscar si ya existen datos para este usuario
    datos = reporteVisitaTecnicaModel.objects.filter(user=request.user).first()

    # si se envia un formulario
    if request.method == 'POST':

        # si existen datos:
        if datos:
            # actualiza el registro existente (instance=datos) arriba
            form = formReporteVisitaTecnica(request.POST, instance=datos) 

        # Si no existen datos, crea uno nuevo
        else:
            form = formReporteVisitaTecnica(request.POST)

        # compruieba si el formulario cumple con las validaciones    
        
        if form.is_valid():
            # si es valido, guarda los datos
            instancia = form.save(commit=False)
            instancia.user = request.user  # Asegúrate de asignar el usuario si es necesario
            instancia.save()
            messages.success(request, 'Datos del Reporte de Visita Tecnica enviados correctamente')
            return redirect('home')
        else:
            messages.error(request, 'Por favor introdusca valores validos.')
            print(form.errors) 
    # si no exsiosten datos:
    else:
        # Si ya existen datos, muestra el formulario con los datos
        if datos:
            form = formReporteVisitaTecnica(instance=datos)
        else:
            form = formReporteVisitaTecnica()

    return render(request, 'Documentos/reporteVisitaTec.html', {
        'form': form,
        'datos': datos
    })

# generar documentos

def wordDeclaratoriaPropiedad(request):
    user = request.user
    datos=get_object_or_404(declaratoriaPropiedadModel, user=user)
    template_path = os.path.join(settings.BASE_DIR, 'Portal', 'templates', 'templatesDocs', 'declaratoriaProp.docx')

    if not os.path.exists(template_path):
        return HttpResponse("La plantilla no existe en la ruta especificada.")

    context = {
        'dueñoDP': datos.dueñoDP,
        'empresaDP': datos.empresaDP,
        'rfcDP': datos.rfcDP,
        'domicilioDP': datos.domicilioDP,
        'emailDP': datos.emailDP,
        'telefonoDP': datos.telefonoDP,
        'reprelegalDP': datos.reprelegalDP,
    }

    print(context)
    doc = DocxTemplate(template_path)
    doc.render(context)

    buffer = BytesIO()  
    doc.save(buffer)
    buffer.seek(0)
    response = HttpResponse(buffer,content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="declaratoria_propiedad_{datos.user}.docx"'
    return response

def wordDeclaratoriaCumplimientoAmbiental(request):
    user = request.user
    datos=get_object_or_404(declaCumpliAmbModel, user=user)
    template_path = os.path.join(settings.BASE_DIR, 'Portal', 'templates', 'templatesDocs', 'declaratoria de Cumplimiento Ambiental.docx')

    if not os.path.exists(template_path):
        return HttpResponse("La plantilla no existe en la ruta especificada.")
    context = {
        'empresaDCA': datos.empresaDCA,
        'domicilioDCA': datos.domicilioDCA,
        'representanteDCA': datos.representanteDCA,
        'rfcDCA': datos.rfcDCA,
        'ubicacionDCA': datos.ubicacionDCA,
        'expedienteDCA': datos.expedienteDCA,
        'responsableDCA': datos.responsableDCA,     
        'cedulaDCA': datos.cedulaDCA,
        'emailDCA': datos.emailDCA,
        'telefonoDCA': datos.telefonoDCA,
        'diaDCA': datos.diaDCA,
        'mesDCA': datos.mesDCA,
        'yearDCA': datos.yearDCA,
    }

    print(context)
    doc = DocxTemplate(template_path)
    doc.render(context)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="declaratoria_cumplimiento_ambiental_{datos.user}.docx"'
    return response

def wordCartaNotificacion(request):
    user = request.user
    datos=get_object_or_404(cartaNotificacionModel, user=user)
    template_path = os.path.join(settings.BASE_DIR, 'Portal', 'templates', 'templatesDocs', 'Carta de Notificacion.docx')

    if not os.path.exists(template_path):
        return HttpResponse("La plantilla no existe en la ruta especificada.")
    context = {
        'lugarCN': datos.lugarCN,
        'diaCN': datos.diaCN,
        'mesCN': datos.mesCN,
        'anioCN': datos.anioCN,
        'nombreNotCN': datos.nombreNotCN,
        'domicilioNotCN': datos.domicilioNotCN,
        'nomRemiCN': datos.nomRemiCN,
        'cargoRemiCN': datos.cargoRemiCN,
        'depaRemiCN': datos.depaRemiCN,
        'motivoCN': datos.motivoCN,
        'objetivoCN': datos.objetivoCN,
        'plazoCN': datos.plazoCN,
        'ubiDepenCN': datos.ubiDepenCN,
        'horarioCN': datos.horarioCN,
        'telDepenCN': datos.telDepenCN,
        'emailDepenCN': datos.emailDepenCN,
    }

    print(context)
    doc = DocxTemplate(template_path)
    doc.render(context)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="Carta-Notificacion-{datos.user}.docx"'
    return response

def wordReporteVisiTec(request):
    user = request.user
    datos=get_object_or_404(reporteVisitaTecnicaModel, user=user)
    template_path = os.path.join(settings.BASE_DIR, 'Portal', 'templates', 'templatesDocs', 'Reporte visita tecnica.docx')

    if not os.path.exists(template_path):
        return HttpResponse("La plantilla no existe en la ruta especificada.")
    
    context = {
        'ciudadRVT': datos.ciudadRVT ,
        'horaRVT': datos.horaRVT,
        'diaRVT': datos.diaRVT ,
        'mesRVT': datos.mesRVT ,
        'yearRVT': datos.yearRVT ,
        'inspectorRVT': datos.inspectorRVT ,
        'cargoRVT': datos.cargoRVT ,
        'departamentoRVT': datos.departamentoRVT ,
        'nomEstableRVT': datos.nomEstableRVT ,
        'direcEstableRVT': datos.direcEstableRVT ,
        'motivoVisitaRVT': datos.motivoVisitaRVT ,
        'condiciSeguRVT': datos.condiciSeguRVT ,
        'manejoResiduosRVT': datos.manejoResiduosRVT ,
        'cumpliNormasRVT': datos.cumpliNormasRVT ,
        'observacionesRVT': datos.observacionesRVT ,
        'nombreResponsRVT': datos.nombreResponsRVT ,
        'tipoIdentificacionRVT': datos.tipoIdentificacionRVT ,
        'numIdentificacionRVT': datos.numIdentificacionRVT ,
        'emailEstableciRVT': datos.emailEstableciRVT ,
        'telefonoEstableciRVT': datos.telefonoEstableciRVT ,
    }

    print(context)
    doc = DocxTemplate(template_path)
    doc.render(context)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="Reporte visita tecnica {datos.user}.docx"'
    return response