# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0002_persontype'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='persontype',
            table='commons_person_type',
        ),
    ]
