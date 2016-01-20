# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20160120_1718'),
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
    ]
