from django.contrib import admin
from .models import Noticia


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor','fecha_publicacion')     # Orden en el que se muestran
    list_filter = ("autor",)                                        # Campo filtrado
    search_fields = ['titulo', 'cuerpo']                            # Campo de búsqueda
    exclude = ('slug',)                                             # Introduce el titulo como slug

admin.site.register(Noticia, NoticiaAdmin)