from django import forms
from django.forms import ModelForm
from .models import datosUsuarioM


class formDatosUsuario(ModelForm):
    class Meta:
        model = datosUsuarioM
        fields = ['propietario', 'email', 'rfc', 'telefono','razonSocial', 'descripcion', 'domicilio']
        labels = {
            'propietario': 'Dueño',
            'email': 'Email',
            'rfc': 'RFC',
            'telefono': 'Telefono',
            'razonSocial': 'Razon social',
            'descripcion': 'Descripcion',
            'domicilio': 'Domicilio',
        }
        widgets = {
            'propietario': forms.TextInput(attrs={'class': 'form-control', 'size':40 , 'placeholder': 'Juan Perez Lopez'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'size':40, 'placeholder': 'exam@ple.com'}),
            'rfc': forms.TextInput(attrs={'class': 'form-control', 'size':40, 'placeholder': 'XXXX000000XXX'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'size':40, 'placeholder': '55-1234-5678'}),
            'razonSocial': forms.TextInput(attrs={'class': 'form-control', 'size':40, 'placeholder': 'Razón social de la empresa'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 4, 'placeholder': 'Descripcion de la empresa'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control', 'size':40, 'placeholder': 'Calle, Numero, Colonia, Ciudad, Estado, CP'}),
            }