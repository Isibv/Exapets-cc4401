from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota
from .forms import MascotaForm
from django.contrib.auth.decorators import login_required


@login_required

def lista_mascotas(request):
    mascotas = Mascota.objects.filter(dueño=request.user)
    return render(request, 'mascotas/mis_mascotas.html', {'mascotas': mascotas})

@login_required

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            mascota = form.save(commit= False)
            mascota.dueño= request.user
            mascota.save()

            return redirect('mascotas:mis_mascotas')
    else:
        form = MascotaForm()
        
    return render(request, 'mascotas/crear_mascota.html', {'form': form})


@login_required

def detalle_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk, dueño=request.user)
    return render(request, 'mascotas/detalle_mascota.html', {'mascota': mascota})


