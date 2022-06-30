from django import views
from django.urls import path
from .views import PublicacionesView, PublicacionDetalladaView

urlpatterns = [
    
    path('', PublicacionesView.as_view(), name="listado-publicaciones"),
    path('detalle/<slug:slug>', PublicacionDetalladaView.as_view(), name="publicacion-detallada"),
    
]
