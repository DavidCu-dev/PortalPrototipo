from django.db import models
from django.contrib.auth.models import User
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