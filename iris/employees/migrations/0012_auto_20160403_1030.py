# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_auto_20160209_2223'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='positionlevel',
            table='employees_position_levels',
        ),
    ]
