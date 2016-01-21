# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20160120_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaddress',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personphone',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
