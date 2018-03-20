# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicine',
            options={'ordering': ['id'], 'verbose_name': 'Medicina', 'verbose_name_plural': 'Medicinas'},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'ordering': ['id'], 'verbose_name': 'Especialidad', 'verbose_name_plural': 'Especialidades'},
        ),
        migrations.AddField(
            model_name='prescribedmedicine',
            name='instructions',
            field=models.CharField(default='N', max_length=1, verbose_name='instrucciones', choices=[('A', 'Antes de comida'), ('C', 'Con la comida'), ('D', 'Despu\xe9s de comer'), ('N', 'Sin instrucciones para comida')]),
        ),
        migrations.AlterField(
            model_name='prescribedmedicine',
            name='frecuency_unit',
            field=models.CharField(max_length=1, verbose_name='unidad de frecuencia', choices=[('H', 'Cada Hora'), ('D', 'Veces al D\xeda')]),
        ),
    ]
