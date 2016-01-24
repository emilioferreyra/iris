# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_auto_20160124_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='depent_of',
            new_name='dependent_of',
        ),
    ]
