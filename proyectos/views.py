from ast import For
from django.shortcuts import render
from .models import Proyecto, Etapa
from django.views.generic import ListView, DetailView

class ProyectosView(ListView):
    model = Proyecto
    template_name = 'proyectos.html'
    ordering = ['-fecha_actualizado']

class ProyectoDetalladoView(DetailView):
    model = Proyecto
    template_name = 'proyecto_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetalladoView, self).get_context_data(**kwargs)
        # Lista de etapas de un proyecto
        lista_etapas = Etapa.objects.filter(proyecto_id=self.kwargs['pk'])
        context['lista_etapas'] = lista_etapas

        # Cálculo del progreso de un proyecto
        suma = 0
        for i in lista_etapas:
            suma += i.progreso
        resultado_progreso = suma/lista_etapas.count()
        context['progreso_proyecto'] = resultado_progreso
        return context


