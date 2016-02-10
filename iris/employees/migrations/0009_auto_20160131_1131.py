# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20160131_1129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostionLevel',
            new_name='PositionLevel',
        ),
        migrations.AlterModelOptions(
            name='positionlevel',
            options={'verbose_name': 'Position Level', 'verbose_name_plural': 'Position Levels'},
        ),
    ]
