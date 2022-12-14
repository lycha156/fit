from django import forms
from .models import Ejercicio, Rutina, Contenedor, Elemento

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