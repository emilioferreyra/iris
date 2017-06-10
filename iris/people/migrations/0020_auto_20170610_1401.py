# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0019_auto_20170610_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='birth_day',
            new_name='birthday',
        ),
    ]
