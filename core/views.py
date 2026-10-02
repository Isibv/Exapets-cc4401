"""Views for the core app: home page and account pages."""
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Landing page of ExaPets, with a short welcome text."""
    
    template_name = "core/home.html"


class UserLoginView(LoginView):
    """Display the login form and sign the user in."""

    template_name = "core/login.html"
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    """Sign the user out (POST only) and redirect to the login page."""
