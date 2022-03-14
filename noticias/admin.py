from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'estado','fecha_creacion')    # Orden en el que se muestran
    list_filter = ("estado",)                                       # Campo filtrado
    search_fields = ['titulo', 'contenido']                         # Campo de búsqueda
    prepopulated_fields = {'slug': ('titulo',) }                     # Introduce el titulo como slug

admin.site.register(Post, PostAdmin)