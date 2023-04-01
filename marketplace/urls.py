from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('publicaciones', views.publicaciones, name='publicaciones'),
    path('publicaciones/crear', views.crear, name='crear'),
    path('publicaciones/editar', views.editar, name='editar'),
    path('eliminar/<int:codigo>', views.eliminar, name='eliminar'),
    path('publicaciones/editar/<int:codigo>', views.editar, name='editar'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
