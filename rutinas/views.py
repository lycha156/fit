from django.shortcuts import render, redirect, get_object_or_404
from .models import Rutina, Ejercicio, Elemento, Contenedor
from agenda.models import Agenda
from socios.models import Socio
import datetime

# RUTINAS
def index(request):

    socio = Socio.objects.get(pk = 1)
    agenda = Agenda.objects.filter(fecha = datetime.date.today()).order_by('fecha')

    context = {
        'fecha_hoy': datetime.date.today(),
        'rutinas': {'socio': 'Mauricio'},
        'socio': socio,
        'agendas': agenda
    }
    return render(request, 'rutinas_index.html', context)

def show(request, id, agenda ):
    socio = Socio.objects.get(pk = id)
    agenda = Agenda.objects.get(pk = agenda )

    context = {
        'socio': socio,
        'agenda': agenda
    }
    return render(request, 'rutinas_show.html', context)

# SERIES

def series_create(request):
    return render(request, 'series/series_create.html')

