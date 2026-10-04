from django.urls import path

from . import views

app_name = 'mascotas'

urlpatterns = [
    path('', views.lista_mascotas, name='mis_mascotas'),
    path('crear/', views.crear_mascota, name='crear_mascota'),
    path('<int:pk>/', views.detalle_mascota, name='detalle_mascota'),
]
