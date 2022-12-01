from django import forms
from .models import Pago
from socios.models import Socio

ESTADO_PAGO = [
        ('PAGO', 'Pago'),
        ('IMPAGO', 'Impago')
    ]

MESES = [
    ('1', '(1) Enero'),
    ('2', '(2) Febrero'),
    ('3', '(3) Marzo'),
    ('4', '(4) Abril'),
    ('5', '(5) Mayo'),
    ('6', '(6) Junio'),
    ('7', '(7) Julio'),
    ('8', '(8) Agosto'),
    ('9', '(9) Septiembre'),
    ('10', '(10) Octubre'),
    ('11', '(11) Noviembre'),
    ('12', '(12) Diciembre'),
]

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = [
            'socio',
            'mes',
            'año',
            'estado',
            'concepto',
            'monto',
            'fechapago'
        ]
    
    # socio = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concepto', 'required': 'required'}), required=False)
    socio = forms.ModelChoiceField(Socio.objects.all(), empty_label=None, widget=forms.Select( attrs={ 'class': 'form-control', 'placeholder': 'Socio'} ))
    mes = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Mes', 'required': 'required', 'autofocus': 'autofocus'}) , choices=MESES)
    año = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'required': 'required'}))
    estado = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado', 'required': 'required'}) , choices=ESTADO_PAGO)
    concepto = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concepto', 'required': 'required'}))
    monto = forms.FloatField( widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto', 'required': 'required'}))
    fechapago = forms.DateField(widget=forms.DateInput(format = ('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}), required=False)

