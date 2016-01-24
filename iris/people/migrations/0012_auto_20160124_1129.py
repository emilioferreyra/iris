# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20160124_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
