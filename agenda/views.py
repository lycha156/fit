from django.shortcuts import render
from .models import Agenda
import datetime

def index(request):
    # inicializar variables
    eventos_json = []
    context = {}

    if request.method == 'POST':
        if request.POST.get('display') == 'dayGridMonth':
            try:
                mes = request.POST.get('mes')
                eventos = Agenda.objects.filter(fecha__month = mes)
                context.update({'initialDate': f'{datetime.date.today().year}-{mes}-01', 'initialView': 'dayGridMonth'})
            except Exception as e:
                print(f'{e}')
        elif request.POST.get('display') == 'timeGridDay':
            try:
                dia = request.POST.get('dia')
                eventos = Agenda.objects.filter(fecha = dia)
                context.update({'initialDate': f'{dia}', 'initialView': 'timeGridDay'})
            except Exception as e:
                print(f'{e}')
    else:
        context.update({'initialDate': f'{datetime.date.today()}', 'initialView': 'dayGridMonth'})
        eventos = Agenda.objects.all()  
    
    # Comportamiento en comun para todos los casos
    # convertir datos en json
    for  evento in eventos:
            eventos_json.append({'title': f'{evento.socio}', 'start': f'{evento.fecha}T{evento.hora}'})

    context.update({'eventos': eventos_json})
    return render(request, 'agenda_index.html', context)
