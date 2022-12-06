# Generated by Django 4.1.3 on 2022-12-06 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socios', '0004_alter_socio_dni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Titulo')),
                ('fecha', models.DateField(verbose_name='Fecha Evento')),
                ('hora', models.TimeField(verbose_name='Hora Evento')),
                ('socio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='socio_pago', to='socios.socio', verbose_name='Socio')),
            ],
        ),
    ]
