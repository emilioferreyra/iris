# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20160203_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personphone',
            name='person_name',
        ),
        migrations.RemoveField(
            model_name='personphone',
            name='phone_ptr',
        ),
        migrations.DeleteModel(
            name='PersonPhone',
        ),
    ]
