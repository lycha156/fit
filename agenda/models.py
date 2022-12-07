from django.db import models
from socios.models import Socio

class Agenda(models.Model):

    class Meta:
        unique_together = ('socio', 'fecha', 'hora')

    socio = models.ForeignKey(Socio, verbose_name="Socio", on_delete=models.RESTRICT, related_name="socio_pago", blank=True, null=True)
    titulo = models.CharField("Titulo", max_length=50, blank=True, null=True)
    fecha = models.DateField("Fecha Evento", auto_now=False, auto_now_add=False)
    hora = models.TimeField("Hora Evento", auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.socio} ({self.fecha}@{self.hora})'