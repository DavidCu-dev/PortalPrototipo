from django import forms
from django.forms import ModelForm
from .models import datosUsuarioM, declaratoriaPropiedadModel, declaCumpliAmbModel, cartaNotificacionModel, reporteVisitaTecnicaModel


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
            'dueñoDP': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'Juan Perez Lopez'}),
            'empresaDP': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'Maderas Lopez S.A. de C.V.'}),
            'rfcDP': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'XXXX000000XXX'}),
            'domicilioDP': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'Calle, Numero, Colonia, Ciudad, Estado, CP'}),
            'emailDP': forms.EmailInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'example@example.com'}),
            'telefonoDP': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:125px;', 'placeholder': '55-1234-5678'}),
            'reprelegalDP': forms.TextInput(attrs={'class': 'form-control d-inline-block text-center', 'style': 'max-width:200px;', 'placeholder': 'Nombre del representante legal'}),
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

class formCartaNotificacion(ModelForm):
    class Meta:
        model = cartaNotificacionModel
        fields = ['lugarCN', 'diaCN', 'mesCN', 'anioCN', 'nombreNotCN', 'domicilioNotCN',
                'nomRemiCN', 'cargoRemiCN', 'depaRemiCN', 'motivoCN', 'objetivoCN',
                'plazoCN', 'ubiDepenCN', 'horarioCN', 'telDepenCN', 'emailDepenCN']
        labels = {
            'lugarCN': 'Lugar',
            'diaCN': 'Día',
            'mesCN': 'Mes',
            'anioCN': 'Año',
            'nombreNotCN': 'Nombre del notificado',
            'domicilioNotCN': 'Domicilio del notificado',
            'nomRemiCN': 'Nombre del remitente',
            'cargoRemiCN': 'Cargo del remitente',
            'depaRemiCN': 'Departamento del remitente',
            'motivoCN': 'Motivo de la notificación',
            'objetivoCN': 'Objetivo de la notificación',
            'plazoCN': 'Plazo para responder',
            'ubiDepenCN': 'Ubicación de la dependencia',
            'horarioCN': 'Horario de atención',
            'telDepenCN': 'Teléfono de la dependencia',
            'emailDepenCN': 'Email de la dependencia',
        }
        widgets = {
            'lugarCN': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'Ciudad, Estado'}),
            'diaCN': forms.TextInput(attrs={'class': 'form-control d-inline-block ', 'style': 'max-width:50px', 'placeholder': 'DD'}),
            'mesCN': forms.TextInput(attrs={'class': 'form-control d-inline-block ', 'style': 'max-width:55px', 'placeholder': 'MM'}),
            'anioCN': forms.TextInput(attrs={'class': 'form-control d-inline-block ', 'style': 'max-width:70px', 'placeholder': 'AAAA'}),
            'nombreNotCN': forms.TextInput(attrs={'class': 'form-control d-inline-block','style': 'max-width:200px;', 'placeholder': 'Nombre del notificado'}),
            'domicilioNotCN': forms.TextInput(attrs={'class': 'form-control d-inline-block','style': 'max-width:300px;', 'placeholder': 'Calle, Numero, Colonia, Ciudad, Estado, CP'}), 
            'nomRemiCN': forms.TextInput(attrs={'class': 'form-control d-inline-block','style': 'max-width:200px;', 'placeholder': 'Nombre del remitente'}),
            'cargoRemiCN': forms.TextInput(attrs={'class': 'form-control d-inline-block','style': 'max-width:200px;', 'placeholder': 'Cargo del remitente'}),    
            'depaRemiCN': forms.TextInput(attrs={'class': 'form-control d-inline-block','style': 'max-width:250px;', 'placeholder': 'Departamento del remitente'}),
            'motivoCN': forms.Textarea(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:500px;', 'rows' : 4, 'placeholder': 'Motivo de la notificación'}),
            'objetivoCN': forms.Textarea(attrs={'class': 'form-control d-inline-block','style': 'max-width:700px;', 'rows' : 4, 'placeholder': 'Objetivo de la notificación'}),
            'plazoCN': forms.TextInput(attrs={'class': 'form-control d-inline-block','style': 'max-width:350px;', 'placeholder': 'Plazo para responder'}),
            'ubiDepenCN': forms.TextInput(attrs={'class': 'form-control d-inline-block','style': 'max-width:250px;', 'placeholder': 'Ubicación de la dependencia'}),
            'horarioCN': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:300px;', 'placeholder': 'Horario de atención'}),
            'telDepenCN': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:150px;', 'placeholder': '55-1234-5678'}),
            'emailDepenCN': forms.EmailInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'example@example.com'}),
        }

class formReporteVisitaTecnica(ModelForm):
    class Meta:
        model = reporteVisitaTecnicaModel
        fields = ['ciudadRVT', 'horaRVT', 'diaRVT', 'mesRVT', 'yearRVT', 'inspectorRVT', 'cargoRVT', 'departamentoRVT', 'nomEstableRVT', 'direcEstableRVT', 'motivoVisitaRVT', 'condiciSeguRVT', 'manejoResiduosRVT', 'cumpliNormasRVT', 'observacionesRVT', 'nombreResponsRVT', 'tipoIdentificacionRVT','numIdentificacionRVT', 'emailEstableciRVT', 'telefonoEstableciRVT']
        labels = {
            'ciudadRVT': 'Ciudad',
            'horaRVT': 'Hora',
            'diaRVT': 'Día',
            'mesRVT': 'Mes',
            'yearRVT': 'Año',
            'inspectorRVT': 'Inspector',
            'cargoRVT': 'Cargo del inspector',
            'departamentoRVT': 'Departamento',
            'nomEstableRVT': 'Nombre del establecimiento',
            'direcEstableRVT': 'Dirección del establecimiento',
            'motivoVisitaRVT': 'Motivo de la visita',
            'condiciSeguRVT': 'Condiciones de seguridad',
            'manejoResiduosRVT': 'Manejo de residuos',
            'cumpliNormasRVT': 'Cumplimiento de normas',
            'observacionesRVT': 'Observaciones',
            'nombreResponsRVT': 'Nombre del responsable del establecimiento',
            'tipoIdentificacionRVT': 'Tipo de identificación',
            'numIdentificacionRVT': 'Número de identificación',
            'emailEstableciRVT': 'Email',
            'telefonoEstableciRVT': 'Teléfono'
        }
        widgets = {
            'ciudadRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'Ciudad'}),
            'horaRVT': forms.TimeInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:100px;', 'type': 'time', 'placeholder': 'HH:MM'}),
            'diaRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:50px;', 'placeholder': 'DD'}),
            'mesRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:55px;', 'placeholder': 'MM'}),
            'yearRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:70px;', 'placeholder': 'AAAA'}),
            'inspectorRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'Nombre del inspector'}),
            'cargoRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'Cargo del inspector'}),
            'departamentoRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block',  'style':'max-width:250px;',  'placeholder':'Departamento del inspector'}),
            'nomEstableRVT': forms.TextInput(attrs={'class':'form-control d-inline-block',  'style':'max-width:250px;',  'placeholder':'Nombre del establecimiento'}),
            'direcEstableRVT': forms.TextInput(attrs={'class':'form-control d-inline-block',  'style':'max-width:300px;',  'placeholder':'Dirección del establecimiento'}),
            'motivoVisitaRVT': forms.Textarea(attrs={'class':'form-control d-inline-block',  'style':'max-width:500px;',  "rows":4,  "placeholder":'Motivo de la visita'}),
            'condiciSeguRVT': forms.Textarea(attrs={'class':'form-control ',  "style":'max-width:500px;',  "rows":4,  "placeholder":'Condiciones de seguridad'}),
            'manejoResiduosRVT': forms.Textarea(attrs={'class':'form-control ',  "style":'max-width:500px;',  "rows":4,  "placeholder":'Manejo de residuos'}),
            'cumpliNormasRVT': forms.Textarea(attrs={'class':'form-control ',  "style":'max-width:500px;',  "rows":4,  "placeholder":'Cumplimiento de normas'}),
            'observacionesRVT': forms.Textarea(attrs={'class':'form-control ',  "style":'max-width:500px;',  "rows":4,  "placeholder":'Observaciones'}),
            'nombreResponsRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'Nombre del responsable'}),
            'tipoIdentificacionRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'Tipo de identificación'}),
            'numIdentificacionRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'Número de identificación'}),
            'emailEstableciRVT': forms.EmailInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:200px;', 'placeholder': 'example@example.com'}),
            'telefonoEstableciRVT': forms.TextInput(attrs={'class': 'form-control d-inline-block', 'style': 'max-width:150px;', 'placeholder': '55-1234-5678'}),
        }