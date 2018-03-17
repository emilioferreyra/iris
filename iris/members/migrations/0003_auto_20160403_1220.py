# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20160403_1219'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='occupation',
            table='members_occupation',
        ),
    ]
