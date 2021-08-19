from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio),
    path('', views.inicio),
    path('agregar',views.agregar),
    path('leer',views.leer),
    path('actualizar',views.actualizar),
    path('eliminar',views.eliminar),
    
]