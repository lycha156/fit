from django import forms
from .models import Ejercicio, Rutina, Contenedor, Elemento
from .models import Rutina, Rutina_modelo, Contenedor_modelo, Elemento_modelo

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
    class Meta:
        model = Elemento
        fields = [
            'contenedor',
            'ejercicio',
            'peso',
            'repeticiones'
        ]

    contenedor = forms.ModelChoiceField(Contenedor.objects.all(), empty_label=None, widget=forms.HiddenInput())
    ejercicio = forms.ModelChoiceField(Ejercicio.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control select2bs4', 'id': 'id_ejercicio'}))
    peso = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    repeticiones = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


# RUTINAS MODELOS
class RutinaModeloForm(forms.ModelForm):
    class Meta:
        model = Rutina_modelo
        fields = [
            'titulo',
            'descripcion'
        ]

    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocuos': 'autofocus'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 110px;'}), required=False)

    def __str__(self):
        return self.titulo