# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_auto_20160121_1919'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='doctoradditionalfield',
            table='doctors_additional_fields',
        ),
    ]
