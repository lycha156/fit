# Generated by Django 4.1.3 on 2022-12-08 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0007_rename_virneshorario_horario_vierneshorario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='socio_horario', to='socios.socio', unique=True, verbose_name='Socio'),
        ),
    ]
