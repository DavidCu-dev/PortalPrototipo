"""
URL configuration for PortalMX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Portal import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('politica_de_privacidad/', views.politicaPrivacidad , name='politicaPrivacidad'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('signin/', views.iniciarSesion, name='iniciarSesion'),
    path('datosUsuario/', views.datosUsuario, name='datosUsuario'),
    path('actDatosUsuario/', views.actualizarDatosUsuario, name='actualizar'),

    # documentos
    path('declaratoria_propiedad/', views.declaratoriaPropiedad, name= 'declaratoriaPropiedad'),
    path('declaratoria_cumplimiento_ambiental/', views.declaratoriaCumplimientoAmbiental, name='declaratoriaCA'),
    path('carta_notificacion/', views.cartaNotificacion, name='cartaNotificacion'),
    path('reporte_visita_tecnica/', views.reporteVisitaTecnica, name='reporteVisitaTecnica'),
    path('inventario_oficina/', views.suplementosOficina, name='inventOfi'),

    # borrar registros
    path('declaratoria_propiedad/delete', views.borrarDP, name='borrarDP'),
    path('declaratoria_cumplimiento_ambiental/delete', views.borrarDCA, name='borrarDCA'),
    path('carta_notificacion/delete', views.borrarCN, name='borrarCN'),
    path('reporte_visita_tecnica/delete', views.borrarRVT, name='borrarRVT'),

    # generaciondoc
    path('declaratoria_propiedad/download/', views.wordDeclaratoriaPropiedad, name='generarDeclaratoria'),
    path('declaratoria_cumplimiento_ambiental/download/', views.wordDeclaratoriaCumplimientoAmbiental, name='generarDeclaratoriaCA'),
    path('carta_notificacion/download/', views.wordCartaNotificacion, name='generarCartaNotificacion'),
    path('reporte_visita_tecnica/download/', views.wordReporteVisiTec, name='generarReporteVT')
]
