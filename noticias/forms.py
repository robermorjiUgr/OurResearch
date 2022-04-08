from django import forms
from .models import Noticia
from taggit.forms import TagWidget
from django.urls import reverse



class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'autor','imagen_principal','fragmento', 'tags', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}), 
            #'autor': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'objetoAutor', 'type':'hidden'}),
            'tags': TagWidget(),
            'fragmento': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Fragmento de artículo'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }
    def get_success_url(self):
        return reverse('noticia-detallada', kwargs={'slug': self.object.slug})

class EditarNoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo','fragmento',  'cuerpo', 'tags')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control col-12 '}),
            'fragmento': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Fragmento de artículo'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': TagWidget(),
        }

   
        
