from django.shortcuts import render, redirect, get_object_or_404
from .models import Agenda
from .forms import AgendaFormTurno, AgendaFormEvento
import datetime
from django.db.models import Q
from django.contrib import messages
from socios.models import Socio, Horario
import calendar

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

# AUTOMATICAMENTE ACTUALIZA LA AGENDA EN BASE A UN MES Y AÑO ESPECIFICADO POR EL USUARIO
# Y LOS DIAS Y HORARIOS ASIGNADOS A LOS SOCIOS ACTIVOS.
def generar_mes(request):

    if request.method == 'POST':
        # inicializar variables
        mesGenerar = request.POST.get('mes')
        añoGenerar = request.POST.get('año')
        socios = Socio.objects.filter(estado = 'ACTIVO')
        diasdelmes = []

        # Generar listado de dias del mes a generar
        calendar.setfirstweekday(calendar.SUNDAY)
        mesTrabajo = calendar.monthcalendar(int(añoGenerar), int(mesGenerar))
        for semana in mesTrabajo:
            for dia in semana:
                if dia != 0:
                    diasdelmes.append({'numero_dia': datetime.date.isoweekday( datetime.date(int(añoGenerar), int(mesGenerar), int(dia)) ), 'dia': datetime.date(int(añoGenerar), int(mesGenerar), int(dia))})

        # Buscar dias por socio y agregar dias a la agenda
        try:
            for socio in socios:
                print(f'{socio}')
                dias_socio = []
                horario = Horario.objects.filter(socio = socio).first()
                if horario.lunes == 1:
                    for dia in diasdelmes:
                        if dia['numero_dia'] == 1:
                            print(f'{socio} => {dia}')
                            # dias_socio.append(dia)
                            Agenda.objects.get_or_create(socio = socio, titulo = None, fecha = dia['dia'], hora = horario.lunesHorario, generadoAuto = True)
                if horario.martes == 1:
                    for dia in diasdelmes:
                        if dia['numero_dia'] == 2:
                            # dias_socio.append(dia)   
                            Agenda.objects.get_or_create(socio = socio,  titulo = None, fecha = dia['dia'], hora = horario.martesHorario, generadoAuto = True)
                if horario.miercoles == 1:
                    for dia in diasdelmes:
                        if dia['numero_dia'] == 3:
                            # dias_socio.append(dia) 
                            Agenda.objects.get_or_create(socio = socio,  titulo = None, fecha = dia['dia'], hora = horario.miercolesHorario, generadoAuto = True)
                if horario.jueves == 1:
                    for dia in diasdelmes:
                        if dia['numero_dia'] == 4:
                            # dias_socio.append(dia)
                            Agenda.objects.get_or_create(socio = socio,  titulo = None, fecha = dia['dia'], hora = horario.juevesHorario, generadoAuto = True) 
                if horario.viernes == 1:
                    for dia in diasdelmes:
                        if dia['numero_dia'] == 5:
                            # dias_socio.append(dia) 
                            Agenda.objects.get_or_create(socio = socio,  titulo = None, fecha = dia['dia'], hora = horario.viernesHorario, generadoAuto = True)
                if horario.sabado == 1:
                    for dia in diasdelmes:
                        if dia['numero_dia'] == 6:
                            # dias_socio.append(dia)   
                            Agenda.objects.get_or_create(socio = socio,  titulo = None, fecha = dia['dia'], hora = horario.sabadoHorario, generadoAuto = True)
                if horario.domingo == 1:
                    for dia in diasdelmes:
                        if dia['numero_dia'] == 7:
                            # dias_socio.append(dia)  
                            Agenda.objects.get_or_create(socio = socio,  titulo = None, fecha = dia['dia'], hora = horario.domingoHorario, generadoAuto = True)                  

            messages.success(request, f'Agenda actualizada para el periodo {mesGenerar}/{añoGenerar}.-')
            return redirect('agenda_index')

        except Exception as e:
            messages.warning(request, f'Error al actualizar la agenda para el periodo {mesGenerar}/{añoGenerar}. Error: {e}.-')
            return redirect('agenda_index')
        
    context = {
        'año': datetime.date.today().year,
        'mes_actual': datetime.date.today().month,
        'meses': MESES
    }
    return render(request, 'agenda_generar_mes.html', context)

MESES = [
    {'id': 1, 'valor': '(1) Enero'},
    {'id': 2, 'valor': '(2) Febrero'},
    {'id': 3, 'valor': '(3) Marzo'},
    {'id': 4, 'valor': '(4) Abril'},
    {'id': 5, 'valor': '(5) Mayo'},
    {'id': 6, 'valor': '(6) Junio'},
    {'id': 7, 'valor': '(7) Julio'},
    {'id': 8, 'valor': '(8) Agosto'},
    {'id': 9, 'valor': '(9) Septiembre'},
    {'id': 10,'valor': '(10) Octubre'},
    {'id': 11,'valor': '(11) Noviembre'},
    {'id': 12,'valor': '(12) Diciembre'},
]