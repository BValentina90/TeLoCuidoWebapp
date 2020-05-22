from django.urls import path, include
from . import views

urlpatterns = [
    path('mapa', views.mapa, name='mapa'),
    path('lugarocupado', views.lugarocupado, name='lugarocupado'),
    path('propina', views.propina, name='propina'),
    path('calificar', views.calificar, name='calificar'),
]
