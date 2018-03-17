# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20160611_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addresstype',
            options={'ordering': ['name'], 'verbose_name': 'Tipo de direcci\xf3n', 'verbose_name_plural': 'Tipo de direcciones'},
        ),
        migrations.AlterModelOptions(
            name='nationality',
            options={'ordering': ['name'], 'verbose_name': 'Nacionalidad', 'verbose_name_plural': 'Nacionalidades'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'ordering': ['name'], 'verbose_name': 'Provincia', 'verbose_name_plural': 'Provincias'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['id'], 'verbose_name': 'Regi\xf3n', 'verbose_name_plural': 'Regiones'},
        ),
        migrations.AlterModelOptions(
            name='town',
            options={'ordering': ['name'], 'verbose_name': 'Municipio', 'verbose_name_plural': 'Municipios'},
        ),
        migrations.AlterField(
            model_name='addresstype',
            name='name',
            field=models.CharField(unique=True, max_length=40, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='province',
            name='region',
            field=models.ForeignKey(default=1, verbose_name='region', to='location.Region'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='town',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='town',
            name='province',
            field=models.ForeignKey(verbose_name='provincia', to='location.Province'),
        ),
    ]
