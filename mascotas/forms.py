from datetime import date

from django import forms

from .models import Mascota


class MascotaForm(forms.ModelForm):
    """Formulario de registro de mascota.

    El dueño (usuario) NO es un campo del formulario: lo asigna la vista
    con request.user, así nadie puede registrar mascotas a nombre de otro.
    """

    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'especie',
            'raza',
            'sexo',
            'fecha_de_nacimiento',
            'peso',
        ]
        labels = {
            'nombre': 'Nombre de la mascota',
            'especie': 'Especie',
            'raza': 'Raza (opcional)',
            'sexo': 'Sexo',
            'fecha_de_nacimiento': 'Fecha de nacimiento (opcional)',
            'peso': 'Peso en kg (opcional)',
        }
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'peso': forms.NumberInput(attrs={'step': '0.01', 'min': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Estilos del sistema de diseño (Bootstrap + styles.css)
        for field in self.fields.values():
            clase = 'form-select' if isinstance(field.widget, forms.Select) else 'form-control'
            field.widget.attrs['class'] = clase
        # El navegador no deja elegir fechas futuras (la validación real está en el modelo)
        self.fields['fecha_de_nacimiento'].widget.attrs['max'] = date.today().isoformat()

    def clean_peso(self):
        """Si se ingresa peso, debe ser mayor a 0."""
        peso = self.cleaned_data.get('peso')
        if peso is not None and peso <= 0:
            raise forms.ValidationError('El peso debe ser un número positivo mayor a 0.')
        return peso
