from dataclasses import fields
from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import  Noticia
from .forms import NoticiaForm, EditarNoticiaForm
from django.urls import reverse_lazy

#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Noticia
    template_name = 'home.html'


class NoticiasView(ListView):
    model = Noticia
    template_name = 'noticias.html'
    ordering = ['-fecha_publicacion']


class NoticiaDetalladaView(DetailView):
    model = Noticia
    template_name = 'noticia_detalle.html'

# CreateView sirve para crear vistas que crean cosas, en este caso una entrada en la BD
class AddNoticiaView(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'add_noticia.html'
    #fields = '__all__'
    #fields = ('titulo','cuerpo')

class UpdateNoticiaView(UpdateView):
    model = Noticia
    form_class = EditarNoticiaForm
    template_name = 'update_noticia.html'

class DeleteNoticiaView(DeleteView):
    model = Noticia
    template_name = 'delete_noticia.html'
    success_url = reverse_lazy('pagina-noticias')



# Vista al pulsar en una etiqueta
def EtiquetaView(request, nombre):
    noticias_etiqueta = Noticia.objects.filter(tags__slug=nombre)
    return render(request, 'etiqueta.html', {'nombre': nombre.replace('-',' '), 'noticias_etiqueta' : noticias_etiqueta})

    
