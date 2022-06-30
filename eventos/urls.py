from django import views
from django.urls import path
from .views import EventosView, EventoDetalladoView

urlpatterns = [
    
    path('', EventosView.as_view(), name="listado-eventos"),
    path('detalle/<int:pk>', EventoDetalladoView.as_view(), name="evento-detallado"),
    
]
