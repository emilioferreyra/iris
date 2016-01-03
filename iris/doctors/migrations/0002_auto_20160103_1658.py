# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctorphones',
            options={'verbose_name': 'Doctor phone', 'verbose_name_plural': 'Doctor phones'},
        ),
        migrations.AlterModelTable(
            name='doctorphones',
            table='doctors_phone',
        ),
    ]
