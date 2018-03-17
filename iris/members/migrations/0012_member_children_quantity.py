# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20170609_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='children_quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
