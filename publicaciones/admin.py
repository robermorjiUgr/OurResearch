from django.contrib import admin
from .models import Publicacion



class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'fecha_publicacion')          # Campo filtrado
    search_fields = ['titulo']                            # Campo de búsqueda
    exclude = ('slug',)                                             # Introduce el titulo como slug

admin.site.register(Publicacion, PublicacionAdmin)
