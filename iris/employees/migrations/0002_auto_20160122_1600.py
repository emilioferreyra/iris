# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmployeeAddress',
        ),
        migrations.DeleteModel(
            name='EmployeePhone',
        ),
    ]
