from django.db import models
from django.core.validators import FileExtensionValidator
from socios.models import Socio

class Documento(models.Model):
    socio = models.ForeignKey(Socio, verbose_name="Socio", on_delete=models.RESTRICT, related_name="socio_documento")
    fecha = models.DateField("Fecha", auto_now=True)
    descripcion = models.TextField("Descripcion")
    documento = models.FileField('Documento', upload_to ="documentos/", null=False, blank=False, validators=[FileExtensionValidator(['pdf', 'jpg', 'png', 'doc', 'docx', 'xlsx'])])
