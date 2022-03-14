from . import views
from django.urls import path


app_name = 'noticias'

urlpatterns = [
    path('', views.home, name='home'),
    path('detalle/', views.detalleNoticia, name='detalle'),
]