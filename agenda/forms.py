from django import forms
from .models import Agenda
from socios.models import Socio

class AgendaFormTurno(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = [
            'socio',
            'titulo',
            'fecha',
            'hora'
        ]

    socio = forms.ModelChoiceField(Socio.objects.all(), empty_label=None, widget=forms.Select( attrs={ 'class': 'form-control select2bs4', 'placeholder': 'Socio'} ))
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}), max_length=100, required=False)
    fecha = forms.DateField(widget=forms.DateInput(format = ('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))

class AgendaFormEvento(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = [
            'socio',
            'titulo',
            'fecha',
            'hora'
        ]

    socio = forms.ModelChoiceField(Socio.objects.all(), empty_label=None, widget=forms.Select( attrs={ 'class': 'form-control', 'placeholder': 'Socio'} ), required=False)
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'autofocus': 'autofocus'}), max_length=100)
    fecha = forms.DateField(widget=forms.DateInput(format = ('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))