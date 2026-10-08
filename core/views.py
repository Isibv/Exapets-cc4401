"""Vistas de la app core: página de inicio y flujo de cuenta (registro, login y logout)."""
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import RegistroForm


class HomeView(TemplateView):
    """Página de inicio de ExaPets, con un texto de bienvenida."""

    template_name = "core/home.html"


class UserLoginView(LoginView):
    """Muestra el formulario de login e inicia la sesión del usuario."""

    template_name = "core/login.html"
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    """Cierra la sesión (solo por POST) y redirige a la página de login."""


def registro(request):
    """Crea una cuenta nueva.

    Si el formulario es válido guarda el usuario y lo envía al login con un
    mensaje de éxito; si no, vuelve a mostrar el formulario con los errores.
    Un usuario que ya inició sesión es enviado directo a sus mascotas.
    """
    if request.user.is_authenticated:
        return redirect("mascotas:mis_mascotas")

    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitosamente. Ya puedes iniciar sesión.")
            return redirect("core:login")
    else:
        form = RegistroForm()

    return render(request, "core/registro.html", {"form": form})
