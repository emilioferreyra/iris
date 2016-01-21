# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20160120_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaddress',
            name='default',
            field=models.BooleanField(default=False, verbose_name=b'Default Address'),
        ),
        migrations.AlterField(
            model_name='personphone',
            name='default',
            field=models.BooleanField(default=False, verbose_name=b'default phone'),
        ),
    ]
