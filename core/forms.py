"""Formularios de la app core (cuenta de usuario)."""
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Usuario


class BootstrapFormMixin:
    """Agrega la clase "form-control" de Bootstrap a todos los campos del formulario."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class LoginForm(BootstrapFormMixin, AuthenticationForm):
    """Formulario de inicio de sesión con el estilo del sistema de diseño."""


class RegistroForm(BootstrapFormMixin, UserCreationForm):
    """Formulario de registro de cuenta.

    El UserCreationForm de Django está atado al modelo User estándar. Como
    este proyecto usa un modelo personalizado (AUTH_USER_MODEL = core.Usuario),
    hay que indicarle explícitamente que cree instancias de Usuario; de lo
    contrario el registro falla al validar o al guardar.
    """

    class Meta(UserCreationForm.Meta):
        model = Usuario
