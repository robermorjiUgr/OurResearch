from django import views
from django.urls import path
from .views import UserEditView, CambiarPasswordView, SobreNosotrosView, MostrarPaginaPerfilView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('edit_perfil/', UserEditView, name="editar-perfil"),
    path('password/', CambiarPasswordView.as_view()),
    path('password_success', views.password_success, name="password_success"),
    path('sobre_nosotros/', SobreNosotrosView.as_view(), name="sobre-nosotros"),
    
    path('<int:pk>/perfil', MostrarPaginaPerfilView.as_view(), name="mostrar_perfil_usuario"),
]
