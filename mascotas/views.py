from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota
from .forms import MascotaForm

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/mis_mascotas.html', {'mascotas': mascotas})

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascotas:mis_mascotas')
    else:
        form = MascotaForm()
        
    return render(request, 'mascotas/crear_mascota.html', {'form': form})

def detalle_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'mascotas/detalle_mascota.html', {'mascota': mascota})