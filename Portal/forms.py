from django import forms
from django.forms import ModelForm
from .models import datosGenerales

class formDatosUsuario(ModelForm):
    class Meta:
        model = datosGenerales
        fields = ['propietario', 'email', 'rfc', 'telefono', 'razonSocial', 'giro', 'domicilio']
        labels = {
            'propietario': 'propietario',
            'email': 'email',
            'rfc': 'rfc',
            'telefono': 'telefono',
            'razonSocial': 'razonSocial',
            'giro': 'giro',
            'domicilio': 'domicilio',
        }
