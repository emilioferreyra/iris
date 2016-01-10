# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
            ],
            options={
                'verbose_name': 'Doctor',
                'proxy': True,
                'verbose_name_plural': 'Doctors',
            },
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='DoctorAddress',
            fields=[
            ],
            options={
                'verbose_name': 'Doctor Address',
                'proxy': True,
                'verbose_name_plural': 'Doctor Addreses',
            },
            bases=('people.personaddress',),
        ),
        migrations.CreateModel(
            name='DoctorPhone',
            fields=[
            ],
            options={
                'verbose_name': 'Doctor Phone',
                'proxy': True,
                'verbose_name_plural': 'Doctor Phones',
            },
            bases=('people.personphone',),
        ),
    ]
