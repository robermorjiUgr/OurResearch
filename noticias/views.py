from django.shortcuts import render

from django.views import generic
from .models import Post

"""
def ultimasNoticias(request):
    queryset = Post.objects.filter(estado=1).order_by('-fecha_creacion')
    context = {'ultimas_noticias': queryset}
    template_name = 'noticias/demo-blog-categories.html'
    return render(request, template_name, context)
"""
def home(request):
    queryset = Post.objects.filter(estado=1).order_by('-fecha_creacion')
    context = {'ultimas_noticias': queryset}
    return render(request, 'noticias/home.html', context )

def detalleNoticia(request):

    return render(request, 'noticias/detalle.html' )

"""
def detalleNoticia(request, slug):
    template_name = 'noticias/demo-blog-single.html'
    context = {'slug': slug}
    return render(request, template_name, context)

"""
