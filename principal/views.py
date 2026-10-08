from django.shortcuts import render, redirect
from .models import Antecedente

mascota = {
        "nombre" : "Maki",
        "especie" : "Perro",
        "raza" : "Schnauzer",
        "edad" : "1 año",
}

# historiales = [
#         {
#             "id": 1,
#             "fecha": "01 Oct 2026",
#             "hora": "10:30",
#             "tipo": "Control Preventivo",
#             "titulo": "Chequeo Sano Anual",
#             "texto": "Paciente en excelente estado. Peso: 8.2 kg. Vacunas al día.",
#         },
#         {
#             "id": 2,
#             "fecha": "15 May 2026",
#             "hora": "16:00",
#             "tipo": "Vacuna",
#             "titulo": "Refuerzo Antirrábica",
#             "texto": "Dosis administrada sin complicaciones secundarias.",
#         },
#     ]


def home(request):
    historiales = Antecedente.objects.all().order_by('-fecha', '-hora')
    context = {
        'mascota' : mascota,
        "historiales" : historiales,
    }

    return render(request, "principal/principal.html", context)


def formulario(request):
    if request.method == 'POST':
        # Captura los datos enviados desde los <input> del HTML
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        tipo = request.POST.get('tipo')
        situacion = request.POST.get('situacion')
        informacion = request.POST.get('informacion')

        # Crea el registro en la base de datos
        Antecedente.objects.create(
            fecha=fecha,
            hora=hora,
            tipo=tipo,
            situacion=situacion,
            informacion=informacion
        )
        return redirect('home') # Vuelve al historial tras guardar

    return render(request, "principal/formulario.html")

