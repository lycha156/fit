from django import forms
from .models import Socio, Cuota

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
    