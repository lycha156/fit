# Generated by Django 4.1.3 on 2022-11-29 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socio',
            old_name='obsevaciones',
            new_name='observaciones',
        ),
    ]
