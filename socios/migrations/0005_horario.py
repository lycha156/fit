# Generated by Django 4.1.3 on 2022-12-08 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0004_alter_socio_dni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunes', models.BooleanField(blank=True, null=True, verbose_name='Lunes')),
                ('lunesHorario', models.TimeField(blank=True, null=True, verbose_name='Horario Lunes')),
                ('martes', models.BooleanField(blank=True, null=True, verbose_name='Martes')),
                ('martesHorario', models.TimeField(blank=True, null=True, verbose_name='Horario Martes')),
                ('miercoles', models.BooleanField(blank=True, null=True, verbose_name='Miercoles')),
                ('miercolesHorario', models.TimeField(blank=True, null=True, verbose_name='Horario Miercoles')),
                ('jueves', models.BooleanField(blank=True, null=True, verbose_name='Jueves')),
                ('juevesHorario', models.TimeField(blank=True, null=True, verbose_name='Horario Jueves')),
                ('viernes', models.BooleanField(blank=True, null=True, verbose_name='Viernes')),
                ('virnesHorario', models.TimeField(blank=True, null=True, verbose_name='Horario Viernes')),
                ('sabado', models.BooleanField(blank=True, null=True, verbose_name='Sabado')),
                ('sabadoHorario', models.TimeField(blank=True, null=True, verbose_name='Horario Sabado')),
                ('domingo', models.BooleanField(blank=True, null=True, verbose_name='Domingo')),
                ('domingoHorario', models.TimeField(blank=True, null=True, verbose_name='Horario Domingo')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='socio_horario', to='socios.socio', verbose_name='Socio')),
            ],
        ),
    ]
