# Generated by Django 4.1.3 on 2022-12-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0002_rename_obsevaciones_socio_observaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='direccion',
            field=models.CharField(blank=True, max_length=50, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='dni',
            field=models.IntegerField(blank=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='fechanacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='telefono',
            field=models.CharField(blank=True, max_length=50, verbose_name='Telefono'),
        ),
    ]
