# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20160122_1006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prescribedmedicine',
            options={'verbose_name': 'Prescription', 'verbose_name_plural': 'Prescriptions'},
        ),
        migrations.AlterField(
            model_name='prescribedmedicine',
            name='frecuency',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='prescribedmedicine',
            name='quantity',
            field=models.FloatField(default=1),
        ),
    ]
