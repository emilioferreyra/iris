# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0020_auto_20170610_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='main_location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
