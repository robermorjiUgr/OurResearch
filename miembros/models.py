from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = RichTextField(blank = True, null=True, default='Cambie este texto')
    cita = models.CharField(max_length=255, null=True, blank=True, default='Cambie este texto')
    rol = models.CharField(max_length=255, null=True, blank=True, default='Cambie este texto')

    imagen_perfil = models.ImageField(null=True, blank=True, upload_to ="images/perfil/")

    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    logros_academicos = models.CharField(max_length=140, null=True, blank=True, default='Cambie este texto')
    logros_laborales = models.CharField(max_length=140, null=True, blank=True, default='Cambie este texto')
    logros_honorificos = models.CharField(max_length=140, null=True, blank=True, default='Cambie este texto')

    def __str__(self):
        return str(self.user)


