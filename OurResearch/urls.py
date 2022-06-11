import imp
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('noticias.urls')),
    path('eventos/', include('eventos.urls')),
    path('proyectos/', include('proyectos.urls')),
    # Este path es necesario para Django
    path('miembros/', include('django.contrib.auth.urls')),
    path('miembros/', include('miembros.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
