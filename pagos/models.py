from django.db import models
from socios.models import Socio

class Pago(models.Model):
    ESTADO_PAGO = [
        ('PAGO', 'Pago'),
        ('IMPAGO', 'Impago')
    ]

    socio = models.ForeignKey(Socio, verbose_name="Socio", on_delete=models.RESTRICT, related_name="socio_agenda")
    mes = models.IntegerField("Mes")
    año = models.IntegerField("Año")
    estado = models.CharField("Estado", max_length=50, choices=ESTADO_PAGO)
    concepto = models.CharField("Concepto", max_length=50)
    monto = models.FloatField("Monto")
    fechapago = models.DateField("Fecha de Pago", blank=True, null=True, auto_now_add=False)

    def __str__(self):
        return f'{self.socio} ({self.mes}/{self.año} - {self.estado}) Concepto: {self.concepto} $ {self.monto}.-'

