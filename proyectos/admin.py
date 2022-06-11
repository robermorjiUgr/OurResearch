from django.contrib import admin
from .models import Etapa, Proyecto

class EtapaInline(admin.TabularInline):
    model = Etapa

class ProyectoAdmin(admin.ModelAdmin):
    inlines = [
        EtapaInline,
    ]

admin.site.register(Proyecto, ProyectoAdmin)