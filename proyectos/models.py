from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from ckeditor.fields import RichTextField



class Proyecto(models.Model):

    titulo = models.CharField(max_length=200, unique=True)

    descripcion = RichTextField(blank=True, null=True, default='Cambie este texto')
    fragmento = models.CharField(max_length=480, default='Cambie este texto')

    imagen_proyecto = models.ImageField(null=True, blank=True, upload_to ="images/proyectos/")

    fecha_creacion = models.DateTimeField(editable=False)
    fecha_actualizado = models.DateTimeField(blank=True, null=True)

    #def get_absolute_url(self):

    #    return reverse("list", args=[self.id])
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.fecha_creacion = timezone.now()
        self.fecha_actualizado = timezone.now()
        return super(Proyecto, self).save(*args, **kwargs)


    def __str__(self):

        return self.titulo


class Etapa(models.Model):

    titulo = models.CharField(max_length=200)

    descripcion = models.TextField(null=True, blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    progreso = models.IntegerField(
        default=0,
        validators=[
            
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)


    def get_absolute_url(self):

        return reverse(

            "item-update", args=[str(self.proyecto.id), str(self.id)]

        )


    def __str__(self):

        return self.titulo


    class Meta:

        ordering = ["fecha_creacion"]