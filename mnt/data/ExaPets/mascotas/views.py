from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Mascota, Tratamiento
from .forms import TratamientoForm

def tratamiento_nuevo(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        form = TratamientoForm(request.POST)
        if form.is_valid():
            tratamiento = form.save(commit=False)
            tratamiento.mascota = mascota
            tratamiento.save()
            return redirect('mascota_detalle', pk=mascota.pk)  # Ajusta al name de URL de la ficha
    else:
        form = TratamientoForm()
    return render(request, 'tratamiento_form.html', {'form': form, 'mascota': mascota})

def agenda(request):
    hoy = timezone.now().date()
    # Próximos inicios y fines de tratamientos desde hoy en adelante
    tratamientos_inicio = Tratamiento.objects.filter(fecha_inicio__gte=hoy).order_by('fecha_inicio')
    tratamientos_fin = Tratamiento.objects.filter(fecha_fin__gte=hoy).order_by('fecha_fin')

    context = {
        'tratamientos_inicio': tratamientos_inicio,
        'tratamientos_fin': tratamientos_fin,
        'hoy': hoy,
    }
    return render(request, 'agenda.html', context)