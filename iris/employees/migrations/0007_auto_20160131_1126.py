# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_remove_employee_employee_level'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmployeeLevel',
            new_name='PostionLevel',
        ),
        migrations.AlterModelOptions(
            name='postionlevel',
            options={'verbose_name': 'Postion Level', 'verbose_name_plural': 'Postion Levels'},
        ),
        migrations.AlterModelTable(
            name='postionlevel',
            table='employees_position_lavels',
        ),
    ]
