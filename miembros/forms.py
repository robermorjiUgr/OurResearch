from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Perfil


class EditarUsuarioForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password')

class EditarPerfilForm(forms.ModelForm):   
    bio = forms.Textarea(attrs={'class': 'form-control'})
    cita = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    rol = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    imagen_perfil = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    logros_academicos = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
    logros_laborales = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
    logros_honorificos = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))

    facebook_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram_url = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Perfil
        fields = ['rol', 'cita', 'bio', 'imagen_perfil', 'logros_academicos', 'logros_laborales', 'logros_honorificos', 'facebook_url', 'twitter_url', 'instagram_url']

class CambiarPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    #last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')