from django.shortcuts import render
from .models import Evento, Ubicacion
from django.views.generic import ListView, DetailView


class EventosView(ListView):
    model = Evento
    template_name = 'eventos.html'
    ordering = ['-fecha_evento']


class EventoDetalladoView(DetailView):
    model = Evento
    template_name = 'evento_detalle.html'

    
    
