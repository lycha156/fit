from django import forms
from .models import Ejercicio, Rutina, Contenedor, Elemento
from .models import Rutina

class EjercicioForm(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = [
            'ejercicio',
            'foto',
            'video'
        ]
    
    ejercicio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}))
    foto = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)
    video = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)


class ContenedorForm(forms.ModelForm):
    model = Contenedor
    fields = [
        # 'rutina',
        'contenedor'
    ]

    # rutina = forms.ModelChoiceField(Rutina.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    contenedor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class ElementoForm(forms.ModelForm):
    model = Elemento
    fields = [
        'contenedor',
        'ejercicio',
        'peso',
        'repeticiones'
    ]

    contenedor = forms.ModelChoiceField(Contenedor.objects.all(), widget=forms.HiddenInput(attrs={'value': None}))
    ejerciio = forms.ChoiceField(Elemento.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-cotnrol'}))
    peso = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), default = 0)
    repeticiones = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), default = 0)