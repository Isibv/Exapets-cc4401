"""Formularios de la app core (cuenta de usuario)."""
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario


class RegistroForm(UserCreationForm):
    """Formulario de registro de cuenta.

    El UserCreationForm de Django está atado al modelo User estándar. Como
    este proyecto usa un modelo personalizado (AUTH_USER_MODEL = core.Usuario),
    hay que indicarle explícitamente que cree instancias de Usuario; de lo
    contrario el registro falla al validar o al guardar.
    """

    class Meta(UserCreationForm.Meta):
        model = Usuario
