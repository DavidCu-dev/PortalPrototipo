from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class datosUsuarioM(models.Model):
    propietario = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    rfc = models.CharField(max_length=13)
    telefono = models.CharField(max_length=30)
    razonSocial = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    domicilio = models.CharField(max_length=255)
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    def __str__(self):
        return self.razonSocial + ' de: '+ self.user.username
def user_directory_path(self):
    return 'user_{0}/{1}'.format(self.user.id, self.original)


class declaratoriaPropiedadModel(models.Model):
    dueñoDP = models.CharField(max_length=255)
    empresaDP = models.CharField(max_length=255)
    rfcDP = models.CharField(max_length=13)
    domicilioDP = models.CharField(max_length=255)
    emailDP = models.EmailField(max_length=255)
    telefonoDP = models.CharField(max_length=30)
    reprelegalDP = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return 'Declaratoria Propidad de: ' + self.user.username
    
class declaCumpliAmbModel(models.Model):
    empresaDCA = models.CharField(max_length=255)
    domicilioDCA = models.CharField(max_length=255)
    representanteDCA = models.CharField(max_length=255)
    rfcDCA = models.CharField(max_length=13)
    ubicacionDCA = models.CharField(max_length=255)
    expedienteDCA = models.CharField(max_length=255)
    responsableDCA = models.CharField(max_length=255)
    cedulaDCA = models.CharField(max_length=255)
    emailDCA = models.EmailField(max_length=255)
    telefonoDCA = models.CharField(max_length=12)
    diaDCA = models.CharField(max_length=2)
    mesDCA = models.CharField(max_length=2)
    yearDCA = models.CharField(max_length=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return 'Declaratoria Cumplimiento Ambiental de: ' + self.user.username
    

class cartaNotificacionModel(models.Model):
    lugarCN = models.CharField(max_length=255)
    diaCN = models.CharField(max_length=2)
    mesCN = models.CharField(max_length=2)
    anioCN = models.CharField(max_length=4)
    nombreNotCN = models.CharField(max_length=255)
    domicilioNotCN = models.CharField(max_length=255)
    nomRemiCN = models.CharField(max_length=255)
    cargoRemiCN = models.CharField(max_length=255)
    depaRemiCN = models.CharField(max_length=255)
    motivoCN = models.TextField(max_length=500)
    objetivoCN = models.TextField(max_length=500)
    plazoCN = models.CharField(max_length=255)
    ubiDepenCN = models.CharField(max_length=255)
    horarioCN = models.CharField(max_length=255)
    telDepenCN = models.CharField(max_length=12)
    emailDepenCN = models.EmailField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return 'Carta de Notificacion de: ' + self.user.username
    
class reporteVisitaTecnicaModel(models.Model):
    ciudadRVT = models.CharField(max_length=255)
    horaRVT = models.TimeField()
    diaRVT = models.CharField(max_length=2)
    mesRVT = models.CharField(max_length=2)
    yearRVT = models.CharField(max_length=4)
    inspectorRVT = models.CharField(max_length=255)
    cargoRVT = models.CharField(max_length=255)
    departamentoRVT = models.CharField(max_length=255)
    nomEstableRVT = models.CharField(max_length=255)
    direcEstableRVT = models.CharField(max_length=255)
    motivoVisitaRVT = models.TextField(max_length=500)
    condiciSeguRVT = models.TextField(max_length=500)
    manejoResiduosRVT = models.TextField(max_length=500)
    cumpliNormasRVT = models.TextField(max_length=500)
    observacionesRVT = models.TextField(max_length=500)
    nombreResponsRVT = models.CharField(max_length=255)
    tipoIdentificacionRVT = models.CharField(max_length=255)
    numIdentificacionRVT = models.CharField(max_length=255)
    emailEstableciRVT = models.EmailField(max_length=255)
    telefonoEstableciRVT = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return 'Reporte de Visita Tecnica de: ' + self.user.username
    

class inventarioOficina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    escriCant= models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    escriModelo = models.CharField(max_length=255)
    escriCondicion = models.CharField(max_length=255)
    escriUbi = models.CharField(max_length=255)
    escriObservaciones = models.TextField(max_length=500)
    sillaCant = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    sillaModelo = models.CharField(max_length=255)
    sillaCondicion = models.CharField(max_length=255)
    sillaUbi = models.CharField(max_length=255)
    sillaObservacion = models.TextField(max_length=500)
    LapCant = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    LapModelo = models.CharField(max_length=255)
    LapCondicion = models.CharField(max_length=255)
    LapUbi = models.CharField(max_length=255)
    LapObservacion = models.TextField(max_length=500)
    proyecCant = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    proyecModelo = models.CharField(max_length=255)
    proyecCondicion = models.CharField(max_length=255)
    proyecUbi = models.CharField(max_length=255)
    proyecObservacion = models.TextField(max_length=500)
    impreCant = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    impreModelo = models.CharField(max_length=255)
    impreCondicion = models.CharField(max_length=255)
    impreUbi = models.CharField(max_length=255)
    impreObservacion = models.TextField(max_length=500)
    aguaCant = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    aguaModelo = models.CharField(max_length=255)
    aguaCondicion = models.CharField(max_length=255)
    aguaUbi = models.CharField(max_length=255)
    aguaObservacion = models.TextField(max_length=500)
    escobCant = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    escobModelo = models.CharField(max_length=255)
    escobCondicion = models.CharField(max_length=255)
    escobUbi = models.CharField(max_length=255)
    escobObservacion = models.TextField(max_length=500)
    extintCant = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    extintModelo = models.CharField(max_length=255)
    extintCondicion = models.CharField(max_length=255)
    extintUbi = models.CharField(max_length=255)
    extintObservacion = models.TextField(max_length=500)
    jabonCant = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    jabonModelo = models.CharField(max_length=255)
    jabonCondicion = models.CharField(max_length=255)
    jabonUbi = models.CharField(max_length=255)
    jabonObservacion = models.TextField(max_length=500)
    hojasCant = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    hojasModelo = models.CharField(max_length=255)
    hojasCondicion = models.CharField(max_length=255)
    hojasUbi = models.CharField(max_length=255)
    hojasObservacion = models.TextField(max_length=500)
    def __str__(self):
        return 'Inventario de oficina de: ' + self.user.username