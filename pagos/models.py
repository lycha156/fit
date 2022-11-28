from django.db import models
from socios.models import Socio

class Cuota(models.Model):
    concepto = models.CharField("Concepto", max_length=50)
    monto = models.FloatField("Monto")

class Pago(models.Model):
    ESTADO_PAGO = [
        ('PAGO', 'Pago'),
        ('IMPAGO', 'Impago')
    ]

    socio = models.ForeignKey(Socio, verbose_name="Socio", on_delete=models.RESTRICT, related_name="socio_pago")
    mes = models.IntegerField("Mes")
    año = models.IntegerField("Año")
    estado = models.CharField("Estado", max_length=50, choices=ESTADO_PAGO)
    monto = models.FloatField("Monto")

