from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente. Ya puedes iniciar sesión.')
            # Redirige a la ruta 'login' que activaste en el paso 3
            return redirect('login') 
    else:
        form = UserCreationForm()
    
    return render(request, 'core/registro.html', {'form': form})
"""Views for the core app: home page and account pages."""


class HomeView(TemplateView):
    """Landing page of ExaPets, with a short welcome text."""
    
    template_name = "core/home.html"


class UserLoginView(LoginView):
    """Display the login form and sign the user in."""

    template_name = "core/login.html"
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    """Sign the user out (POST only) and redirect to the login page."""
