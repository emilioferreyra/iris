# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0018_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='father_last_name',
            field=models.CharField(max_length=50, verbose_name='Primer Apellido'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(help_text='Seleccione g\xe9nero', max_length=1, null=True, verbose_name='g\xe9nero', choices=[('M', 'Masculino'), ('F', 'Femenino')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='mother_last_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Segundo Apellido', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='names',
            field=models.CharField(max_length=100, verbose_name='nombres'),
        ),
    ]
