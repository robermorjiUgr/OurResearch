from django.urls import path
from .views import AddNoticiaView, HomeView, NoticiaDetalladaView, NoticiasView, AddNoticiaView, UpdateNoticiaView, DeleteNoticiaView, EtiquetaView

urlpatterns = [
    #path('',views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('noticias/', NoticiasView.as_view(), name="pagina-noticias"),
    path('noticia/<slug:slug>', NoticiaDetalladaView.as_view(), name="noticia-detallada"),
    path('add_noticia/', AddNoticiaView.as_view(), name="add-noticia"),
    path('noticia/editar/<slug:slug>', UpdateNoticiaView.as_view(), name="update-noticia"),
    path('noticia/borrar/<slug:slug>', DeleteNoticiaView.as_view(), name="delete-noticia"),
    path('etiqueta/<str:nombre>', EtiquetaView, name="etiqueta"),
]
