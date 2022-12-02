from django import forms
from .models import Documento
from socios.models import Socio

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'socio',
            'descripcion',
            'documento'
        ]

    socio = forms.ModelChoiceField(Socio.objects.all(), empty_label=None, required=False, widget=forms.Select( attrs={ 'class': 'form-control', 'placeholder': 'Socio'} ))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 8rem;'}), required=False)
    documento = forms.FileField(label="Seleccione archivo pinche wey" ,required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))