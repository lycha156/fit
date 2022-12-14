from django.db import models
from django.core.validators import FileExtensionValidator
from socios.models import Socio
from agenda.models import Agenda

# RUTINAS
class Rutina(models.Model):
    socio = models.ForeignKey(Socio, verbose_name="Socio", on_delete=models.CASCADE, related_name="rutina_socio")
    agenda = models.ForeignKey(Agenda, verbose_name="Agenda", on_delete=models.CASCADE, related_name="rutina_agenda")

    class Meta:
        unique_together = ('socio', 'agenda')

    def __str__(self):
        return f'{self.socio} - {self.agenda.fecha}'

# CONTENEDORES
class Contenedor(models.Model):
    rutina = models.ForeignKey('rutinas.Rutina', verbose_name="Rutina", on_delete=models.CASCADE, related_name="contenedor_rutina")
    contenedor = models.CharField("Serie", max_length=50)

# ELEMENTOS_CONTENEDOR
class Elemento(models.Model):
    contenedor = models.ForeignKey('rutinas.Contenedor', verbose_name="Contenedor", on_delete=models.CASCADE, related_name="elemento_contenedor")
    ejercicio = models.ForeignKey('rutinas.Ejercicio', verbose_name="Ejercicio", on_delete=models.RESTRICT, related_name="elemento_ejercicio")
    peso = models.FloatField("Peso", default = 0)
    repeticiones = models.IntegerField("Repeticiones", default = 0)

    def __str__(self):
        return f'{self.ejercicio}'

# EJERCICIOS
class Ejercicio(models.Model):
    
    ejercicio = models.CharField("Ejercicio", max_length=50)
    foto = models.FileField('Foto', upload_to ="documentos/ejercicios/fotos/", null=False, blank=False, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]) 
    video = models.FileField('Video', upload_to ="documentos/ejercicios/videos/", null=False, blank=False, validators=[FileExtensionValidator(['avi', 'mp4'])])

    def __str__(self):
        return f'{self.ejercicio}'

# -------------------------- MODELOS DE RUTINAS --------------------------

# RUTINA MODELO
class Rutina_modelo(models.Model):
    titulo = models.CharField("Titulo", max_length=100)
    descripcion = models.TextField("Descripcion")

    def __str__(self):
        return self.titulo

# SERIE MODELO
class Contenedor_modelo(models.Model):
    rutina = models.ForeignKey('rutinas.Rutina_modelo', verbose_name="Rutina", on_delete=models.CASCADE, related_name="contenedor_rutina_modelo")
    contenedor = models.CharField("Serie", max_length=50)

# ELEMENTOS_CONTENEDOR MODELO
class Elemento_modelo(models.Model):
    contenedor = models.ForeignKey('rutinas.Contenedor_modelo', verbose_name="Contenedor", on_delete=models.CASCADE, related_name="elemento_Contenedor_modelo")
    ejercicio = models.ForeignKey('rutinas.Ejercicio', verbose_name="Ejercicio", on_delete=models.RESTRICT, related_name="ejercicio_elemento_modelo")
    peso = models.FloatField("Peso", default = 0)
    repeticiones = models.IntegerField("Repeticiones", default = 0)

    def __str__(self):
        return f'{self.ejercicio}'