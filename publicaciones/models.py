from django.db import models
from django.template.defaultfilters import slugify
from miembros.models import Perfil
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.dispatch import receiver
from django.db.models.signals import pre_save
import string, random

class Publicacion(models.Model):

    titulo = models.CharField(max_length=255)
    fecha_publicacion = models.DateField(null=True, blank=True, auto_now_add=True)
    participantes = models.ManyToManyField(Perfil, blank=True)
    resumen = RichTextField(blank = True, null=True)
    imagen_principal = models.ImageField(null=True, blank=True, upload_to ="images/publicaciones/")
    archivo = models.FileField(null=True, blank=True, upload_to = "pdfs/publicaciones/")
    slug= models.SlugField(max_length=500, unique=True, null=True, blank=True)
    tags = TaggableManager()


    def __str__(self):

        return self.titulo


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.titulo)

    class_ = instance.__class__
    qs_exists = class_.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = f"{slug}-{random_string_generator(size=5)}"
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

@receiver(pre_save, sender=Publicacion)
def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    