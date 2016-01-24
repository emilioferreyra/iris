# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20160124_0954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='parent_of',
            new_name='depent_of',
        ),
    ]
