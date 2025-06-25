from django import forms
from django.forms import ModelForm
from .models import datosUsuarioM, declaratoriaPropiedadModel, declaCumpliAmbModel


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
        
class formDeclaratoriaPropiedad(ModelForm):
    class Meta:
        model = declaratoriaPropiedadModel
        fields = ['dueñoDP', 'empresaDP', 'rfcDP', 'domicilioDP', 'emailDP', 'telefonoDP', 'reprelegalDP']
        labels = {
            'dueñoDP': 'Dueño',
            'empresaDP': 'Empresa',
            'rfcDP': 'RFC',
            'domicilioDP': 'Domicilio',
            'emailDP': 'Email',
            'telefonoDP': 'Telefono',
            'reprelegalDP': 'Representante legal',
        }
        widgets = {
            'dueñoDP': forms.TextInput(attrs={'size':15, 'placeholder': 'Juan Perez Lopez'}),
            'empresaDP': forms.TextInput(attrs={'size':25, 'placeholder': 'Maderas Lopez S.A. de C.V.'}),
            'rfcDP': forms.TextInput(attrs={'size':13, 'placeholder': 'XXXX000000XXX'}),
            'domicilioDP': forms.TextInput(attrs={'size':40, 'placeholder': 'Calle, Numero, Colonia, Ciudad, Estado, CP'}),
            'emailDP': forms.EmailInput(attrs={'size':20, 'placeholder': 'example@example.com'}),
            'telefonoDP': forms.TextInput(attrs={'size':12, 'placeholder': '55-1234-5678'}),
            'reprelegalDP': forms.TextInput(attrs={'size':15, 'placeholder': 'Nombre del representante legal'}),
        }

class formDeclaratoriaCumplimientoAmbiental(ModelForm):
    class Meta:
        model = declaCumpliAmbModel
        fields = ['empresaDCA', 'domicilioDCA', 'representanteDCA', 'rfcDCA', 'ubicacionDCA', 'expedienteDCA',
                'responsableDCA', 'cedulaDCA', 'emailDCA', 'telefonoDCA', 'diaDCA', 'mesDCA', 'yearDCA']
        labels = {
            'empresaDCA': 'Empresa',
            'domicilioDCA': 'Domicilio',
            'representanteDCA': 'Representante',
            'rfcDCA': 'RFC',
            'ubicacionDCA': 'Ubicación',
            'expedienteDCA': 'Expediente',
            'responsableDCA': 'Responsable',
            'cedulaDCA': 'Cédula',
            'emailDCA': 'Email',
            'telefonoDCA': 'Teléfono',
            'diaDCA': 'Día',
            'mesDCA': 'Mes',
            'yearDCA': 'Año',
        }
        widgets = {
            'empresaDCA': forms.TextInput(attrs={'size':25, 'placeholder': 'Maderas Lopez S.A. de C.V.'}),
            'domicilioDCA': forms.TextInput(attrs={'size':40, 'placeholder': 'Calle, Numero, Colonia, Ciudad, Estado, CP'}),
            'representanteDCA': forms.TextInput(attrs={'size':15, 'placeholder': 'Nombre del representante legal'}),
            'rfcDCA': forms.TextInput(attrs={'size':13, 'placeholder': 'XXXX000000XXX'}),
            'ubicacionDCA': forms.TextInput(attrs={'size':40, 'placeholder': 'Ubicación de la empresa'}),
            'expedienteDCA': forms.TextInput(attrs={'size':20, 'placeholder': 'Número de expediente'}),
            'responsableDCA': forms.TextInput(attrs={'size':15, 'placeholder': 'Nombre del responsable'}),
            'cedulaDCA': forms.TextInput(attrs={'size':20, 'placeholder': 'Número de cédula profesional'}),
            'emailDCA': forms.EmailInput(attrs={'size':20, 'placeholder': 'example@example.com'}),
            'telefonoDCA': forms.TextInput(attrs={'size':12, 'placeholder': '55-1234-5678'}),
            'diaDCA': forms.TextInput(attrs={'size':2, 'placeholder': 'DD'}),
            'mesDCA': forms.TextInput(attrs={'size':2, 'placeholder': 'MS'}),
            'yearDCA': forms.TextInput(attrs={'size':4, 'placeholder': 'AAAA'}),
        }