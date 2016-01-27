# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees', 'permissions': (('add_employee', 'Can add Employee'), ('change_employee', 'Can change Employee'), ('delete_employee', 'Can delete Employee'))},
        ),
    ]
