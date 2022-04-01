from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('noticias.urls')),
    # Este path es necesario para Django
    path('miembros/', include('django.contrib.auth.urls')),
    path('miembros/', include('miembros.urls')),
]
