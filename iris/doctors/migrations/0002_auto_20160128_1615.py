# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='province',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='region',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='town',
        ),
        migrations.DeleteModel(
            name='Clinic',
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Clinic',
                'proxy': True,
                'verbose_name_plural': 'Clinics',
            },
            bases=('suppliers.suppliercompany',),
        ),
    ]
