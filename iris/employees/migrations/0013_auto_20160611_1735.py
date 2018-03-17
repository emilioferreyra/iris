# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0012_auto_20160403_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeetype',
            options={'ordering': ['name'], 'verbose_name': 'Tipo de empleado', 'verbose_name_plural': 'Tipos de empleados'},
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
    ]
