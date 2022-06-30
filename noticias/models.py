from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
import string, random
from django.dispatch import receiver
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField


class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen_principal = models.ImageField(null=True, blank=True, upload_to ="images/")
    #cuerpo = models.TextField()
    fragmento = models.CharField(max_length=255)
    cuerpo = RichTextField(blank = True, null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    tags = TaggableManager()
    slug= models.SlugField(max_length=500, unique=True, null=True, blank=True)
    
    # Esto permite ver el título y el autor desde la página admin.
    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    # Método que permite redirigir después de publicar una noticia.
    def get_absolute_url(self):
        return reverse('noticia-detallada', kwargs={'slug': self.slug})

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

@receiver(pre_save, sender=Noticia)
def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)