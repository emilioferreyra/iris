# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
            ],
            options={
                'verbose_name': 'Employee',
                'proxy': True,
                'verbose_name_plural': 'Employees',
            },
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='EmployeeAddress',
            fields=[
            ],
            options={
                'verbose_name': 'Employee Address',
                'proxy': True,
                'verbose_name_plural': 'Employee Addreses',
            },
            bases=('people.personaddress',),
        ),
        migrations.CreateModel(
            name='EmployeePhone',
            fields=[
            ],
            options={
                'verbose_name': 'Employee Phone',
                'proxy': True,
                'verbose_name_plural': 'Employee Phones',
            },
            bases=('people.personphone',),
        ),
    ]
