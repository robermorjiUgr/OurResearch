from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Borrador"),
    (1,"Publicado")
)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE,related_name='noticia')
    fecha_publicacion = models.DateTimeField(auto_now= True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
