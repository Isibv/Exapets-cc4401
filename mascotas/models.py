from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


OPCIONES_SEXO= [
    ("M","Macho"), #M lo que ve la bd y Macho lo que ve el usuario
    ("H", "Hembra"),
    ("D", "Desconocido"),
]

todayDate = timezone.localdate 

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100,null = True, blank = True)
    sexo = models.CharField(max_length= 1,choices=OPCIONES_SEXO)
    fecha_de_nacimiento = models.DateField(null = True, blank = True, validators=[MaxValueValidator(todayDate)])
    peso = models.FloatField(null = True, blank = True, validators=[MinValueValidator(0)])
    #DEFINIR MODELO DE USUARIO CON BLOQUE A
    #dueño = models.ForeignKey(???, on_delete = models.CASCADE)


         