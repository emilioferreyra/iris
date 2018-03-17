# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employeelevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_lavel',
            field=models.ForeignKey(to='employees.EmployeeLevel', null=True),
        ),
    ]
