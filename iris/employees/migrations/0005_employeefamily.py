# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20160124_1036'),
        ('employees', '0004_auto_20160124_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeFamily',
            fields=[
            ],
            options={
                'verbose_name': 'Employee Family',
                'proxy': True,
                'verbose_name_plural': 'Employee Families',
            },
            bases=('people.person',),
        ),
    ]
