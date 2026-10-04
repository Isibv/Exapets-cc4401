from django.db import models
from django.core.exceptions import ValidationError

class Tratamiento(models.Model):
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE, related_name="tratamientos")
    medicamento = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)  # Ej. "cada 8 horas"
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def clean(self):
        if self.fecha_fin and self.fecha_fin < self.fecha_inicio:
            raise ValidationError("La fecha de fin no puede ser anterior al inicio.")

    def __str__(self):
        return f"{self.medicamento} - {self.mascota.nombre}"