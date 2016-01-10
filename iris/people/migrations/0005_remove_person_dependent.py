# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_kinsman'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='dependent',
        ),
    ]
