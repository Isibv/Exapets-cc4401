"""Views for the core app: home page and account pages."""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Landing page of ExaPets, with a short welcome text."""
    
    template_name = "core/home.html"

# Create your views here.
