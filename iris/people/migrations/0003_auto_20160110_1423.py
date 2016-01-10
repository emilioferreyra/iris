# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20160110_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='father_name',
            new_name='father_last_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='mother_name',
            new_name='mother_last_name',
        ),
    ]
