from django import forms
from .models import Noticia
from taggit.forms import TagWidget
from django.urls import reverse



class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'autor', 'tags', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'tags': TagWidget(),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }
    def get_success_url(self):
        return reverse('noticia-detallada', kwargs={'slug': self.object.slug})

class EditarNoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo',  'cuerpo', 'tags')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control col-12 '}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': TagWidget(),
        }

   
        
