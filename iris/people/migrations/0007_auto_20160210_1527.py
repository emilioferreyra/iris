# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20160204_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaddress',
            old_name='default',
            new_name='is_default',
        ),
        migrations.RenameField(
            model_name='personphone',
            old_name='default',
            new_name='is_default',
        ),
    ]
