# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_employee_lavel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employee_lavel',
            new_name='employee_level',
        ),
    ]
