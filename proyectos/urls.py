from django import views
from django.urls import path
from .views import ProyectosView, ProyectoDetalladoView

urlpatterns = [
    
    path('', ProyectosView.as_view(), name="listado-proyectos"),
    path('detalle/<int:pk>', ProyectoDetalladoView.as_view(), name="proyecto-detallado"),
    
]
