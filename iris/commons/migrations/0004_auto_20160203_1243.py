# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20160203_1243'),
        ('commons', '0003_auto_20160128_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='phone_type',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]
