# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_personaddress_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaddress',
            old_name='Location',
            new_name='location',
        ),
    ]
