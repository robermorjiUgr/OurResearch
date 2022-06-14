from django.shortcuts import render
from .models import Publicacion
from django.views.generic import ListView, DetailView

class PublicacionesView(ListView):
    model = Publicacion
    template_name = 'publicaciones.html'
    ordering = ['-fecha_publicacion']

class PublicacionDetalladaView(DetailView):
    model = Publicacion
    template_name = 'publicacion_detalle.html'

    def get_context_data(self, **kwargs):
        publicaciones_relacionadas = self.object.tags.similar_objects()
        context = super(PublicacionDetalladaView, self).get_context_data(**kwargs)
        context['publicaciones_relacionadas'] = publicaciones_relacionadas
        return context

    


