from django import forms
from .models import Socio, Cuota, Horario

class CuotaForm(forms.ModelForm):
    class Meta:
        model = Cuota
        fields = [
            'concepto',
            'monto'
        ]

    concepto = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concepto', 'required': 'required', 'autofocus': 'autofocus'}))
    monto = forms.FloatField( widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto', 'required': 'required'}))

ESTADO_SOCIO = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo')
    ]

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = [
            'apellido',
            'nombre',
            'fechanacimiento',
            'dni',
            'telefono',
            'direccion',
            'email',
            'estado',
            'observaciones',
            'cuota'
        ]

    apellido = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'required': 'required', 'autofocus': 'autofocus'}))
    nombre = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'required': 'required'}))
    fechanacimiento = forms.DateField(widget=forms.DateInput(format = ('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}) , required=False)
    dni = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}), required=False)
    telefono = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}), required=False)
    direccion = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email', 'type': 'email'}), required=False)
    estado = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado'}) , choices=ESTADO_SOCIO)
    cuota = forms.ModelChoiceField(Cuota.objects.all(), empty_label=None, widget=forms.Select( attrs={ 'class': 'form-control', 'placeholder': 'Tipo de Cuota'} ))
    observaciones = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 8rem;'}), required=False)
    

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            # 'socio',
            'lunes',
            'lunesHorario',
            'martes',
            'martesHorario',
            'miercoles',
            'miercolesHorario',
            'jueves',
            'juevesHorario',
            'viernes',
            'viernesHorario',
            'sabado',
            'sabadoHorario',
            'domingo',
            'domingoHorario'
        ]

    # socio = forms.ModelChoiceField(Socio.objects.all(), empty_label=None, widget=forms.Select( attrs={ 'class': 'form-control', 'placeholder': 'Socio'} ), required=False)
    lunes = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    lunesHorario = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}), required=False)
    martes = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    martesHorario = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}), required=False)
    miercoles = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    miercolesHorario = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}), required=False)
    jueves = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    juevesHorario = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}), required=False)
    viernes = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    viernesHorario = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}), required=False)
    sabado = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    sabadoHorario = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}), required=False)
    domingo = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    domingoHorario = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}), required=False)