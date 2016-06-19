# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20160611_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'Vivienda', 'verbose_name_plural': 'Caracter\xedsticas de la Vivienda'},
        ),
        migrations.AlterModelOptions(
            name='memberfamily',
            options={'verbose_name': 'Familiar del miembro', 'verbose_name_plural': 'Familiares del miembro'},
        ),
        migrations.AlterField(
            model_name='house',
            name='floor',
            field=models.ForeignKey(verbose_name='piso', to='housing.HouseMaterialFloor', help_text='Seleccione piso'),
        ),
        migrations.AlterField(
            model_name='house',
            name='property_type',
            field=models.ForeignKey(verbose_name='Tipo de propiedad', to='housing.PropertyType', help_text='Seleccione tipo de propiedad'),
        ),
        migrations.AlterField(
            model_name='member',
            name='where_work',
            field=models.CharField(help_text='Empresa o lugar donde trabaja', max_length=100, null=True, verbose_name='donde trabaja', blank=True),
        ),
    ]
