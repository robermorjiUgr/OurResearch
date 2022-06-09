from email.policy import default
from django.db import models
from django.forms import IntegerField, NumberInput
from ckeditor.fields import RichTextField
from miembros.models import Perfil
from phonenumber_field.modelfields import PhoneNumberField


class Ubicacion(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=300)
    codigo_postal = models.CharField(max_length=10)
    telefono = PhoneNumberField(null=False, blank=False, unique=True)
    web = models.URLField()
    correo_electronico = models.EmailField()
    imagen_ubicacion = models.ImageField(null=True, blank=True, upload_to ="images/ubicaciones/")

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField( max_length=120)
    fecha_evento = models.DateTimeField()
    ubicacion = models.ForeignKey(
        Ubicacion,  null=False, on_delete=models.CASCADE)
    descripcion = RichTextField(
        blank=True, null=True, default='Cambie este texto')
    participantes = models.ManyToManyField(Perfil, blank=True)
    imagen_evento = models.ImageField(null=True, blank=True, upload_to ="images/eventos/")
    aforo = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.nombre
