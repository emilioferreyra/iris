# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20160112_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mother_last_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
