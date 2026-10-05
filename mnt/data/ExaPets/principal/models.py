from django.db import models

class Antecedente(models.Model):
    # mascota = models.ForeignKey('mascotas.Mascota', on_delete=models.CASCADE)
    
    fecha = models.DateField()
    hora = models.TimeField()
    tipo = models.CharField(max_length=100)
    situacion = models.CharField(max_length=200)
    informacion = models.TextField()

    def __str__(self):
        return f"{self.fecha} - {self.situacion}"