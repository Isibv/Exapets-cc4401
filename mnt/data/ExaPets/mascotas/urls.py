from django.urls import path
from . import views

urlpatterns = [
    path("mascotas/<int:pk>/tratamiento/nuevo/", views.tratamiento_nuevo, name="tratamiento_nuevo"),
    path("agenda/", views.agenda, name="agenda"),
]