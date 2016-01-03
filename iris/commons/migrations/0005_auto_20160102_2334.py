# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0004_academiclevel'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='academiclevel',
            table='commons_academic_level',
        ),
    ]
