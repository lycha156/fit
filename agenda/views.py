from django.shortcuts import render, redirect, get_object_or_404
from .models import Agenda
from .forms import AgendaFormTurno, AgendaFormEvento
import datetime
from django.db.models import Q
from django.contrib import messages

def index(request):
    # inicializar variables
    eventos_json = []
    context = {}

    if request.method == 'POST':
        if request.POST.get('display') == 'dayGridMonth':
            try:
                mes = request.POST.get('mes')
                año = request.POST.get('año')
                eventos = Agenda.objects.filter( Q(fecha__month = mes) & Q(fecha__year = año))
                context.update({'initialDate': f'{año}-{mes}-01', 'initialView': 'dayGridMonth'})
                print(context)
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
        if evento.socio == None:
            eventos_json.append({'id': f'evento/{evento.id}', 'title': f'{evento.titulo}', 'start': f'{evento.fecha}T{evento.hora}', 'backgroundColor': '#e75353', 'borderColor': '#e75353'})
        else:
            eventos_json.append({'id': f'turno/{evento.id}', 'title': f'{evento.socio}', 'start': f'{evento.fecha}T{evento.hora}', 'backgroundColor': 'blue'})


    context.update({'eventos': eventos_json, 'año': datetime.date.today().year})
    return render(request, 'agenda_index.html', context)

def create_turno(request):
    form = AgendaFormTurno(request.POST or None)

    if form.is_valid():
        try:
            instancia = form.save()
            messages.success(request, f'Turno de {instancia.socio} para el dia {instancia.fecha} - {instancia.hora}Hs fue cargado con exit.-')
            return redirect('agenda_index') 
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('agenda_index') 

    context = {
        'form': form
    }
    return render(request, 'agenda_create_turno.html', context)

def create_evento(request):
    form = AgendaFormEvento(request.POST or None)

    if form.is_valid():
        try:
            instancia = form.save()
            messages.success(request, f'El evento "{instancia.titulo}" para el dia {instancia.fecha} - {instancia.hora}Hs fue cargado con exit.-')
            return redirect('agenda_index') 
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('agenda_index') 

    context = {
        'form': form
    }
    return render(request, 'agenda_create_evento.html', context)

def update(request, evento, id=id):

    if evento == 'turno':
        obj = get_object_or_404(Agenda, pk=id)
        form = AgendaFormTurno(request.POST or None, instance=obj)

        if form.is_valid():
            try:
                instancia = form.save()
                messages.success(request, f'El turno de "{instancia.socio}" para el dia {instancia.fecha} - {instancia.hora}Hs fue actualizado con exit.-')
                return redirect('agenda_index')
            except Exception as e:
                messages.warning(request, f'Error al actualizar los datos. {e}')
                return redirect('agenda_index')
        
        context = {
            'form': form,
            'borrar': True,
            'evento_id': obj.id
        }
        return render(request, 'agenda_create_turno.html', context)
    
    if evento == 'evento':
        obj = get_object_or_404(Agenda, pk=id)
        form = AgendaFormEvento(request.POST or None, instance=obj)

        if form.is_valid():
            try:
                instancia = form.save()
                messages.success(request, f'El evento "{instancia.titulo}" para el dia {instancia.fecha} - {instancia.hora}Hs fue actualizado con exit.-')
                return redirect('agenda_index')
            except Exception as e:
                messages.warning(request, f'Error al actualizar los datos. {e}')
                return redirect('agenda_index')
        
        context = {
            'form': form,
            'borrar': True,
            'evento_id': obj.id
        }
        return render(request, 'agenda_create_evento.html', context)

def delete(request, id=id):
    agenda = get_object_or_404(Agenda, pk=id)

    try:
        agenda.delete()
        messages.success(request, 'Evento eliminado con exito.-')
        return redirect('agenda_index')
    except Exception as e:
        messages.warning(request, f'Error al eliminar los datos. Erros: {e}.-')
        return redirect('agenda_index')

def generar_mes(request):

    context = {
        'año': datetime.date.today().year
    }
    return render(request, 'agenda_generar_mes.html', context)