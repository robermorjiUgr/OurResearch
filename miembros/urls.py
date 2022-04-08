from django import views
from django.urls import path
from .views import UserEditView, CambiarPasswordView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('edit_perfil/', UserEditView.as_view(), name="editar-perfil"),
    path('password/', CambiarPasswordView.as_view()),
    path('password_success', views.password_success, name="password_success"),
    
]
