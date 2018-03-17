# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0006_auto_20160403_1217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='housematerial',
            options={'ordering': ['id'], 'verbose_name': 'Material de la vivienda', 'verbose_name_plural': 'Martiales de la vivienda'},
        ),
        migrations.AlterModelOptions(
            name='housematerialceiling',
            options={'verbose_name': 'Material del Techo', 'verbose_name_plural': 'Materiales del Techo'},
        ),
        migrations.AlterModelOptions(
            name='housematerialfloor',
            options={'verbose_name': 'Material del piso', 'verbose_name_plural': 'Materiales del piso'},
        ),
        migrations.AlterModelOptions(
            name='housematerialwall',
            options={'verbose_name': 'Material de la pared', 'verbose_name_plural': 'Materiales de la pared'},
        ),
        migrations.AlterModelOptions(
            name='housepart',
            options={'ordering': ['id'], 'verbose_name': 'Parte de la vivienda', 'verbose_name_plural': 'Partes de la vivienda'},
        ),
        migrations.AlterModelOptions(
            name='propertytype',
            options={'ordering': ['id'], 'verbose_name': 'Tipo de propiedad', 'verbose_name_plural': 'Tipos de propiedades'},
        ),
        migrations.AlterField(
            model_name='housematerial',
            name='house_part',
            field=models.ForeignKey(verbose_name='parte de casa', to='housing.HousePart'),
        ),
        migrations.AlterField(
            model_name='housematerial',
            name='name',
            field=models.CharField(max_length=20, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='housepart',
            name='name',
            field=models.CharField(unique=True, max_length=20, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='propertytype',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
    ]
