# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_auto_20160131_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_level',
        ),
    ]
