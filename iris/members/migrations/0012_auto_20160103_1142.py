# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20160103_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kinsman',
            name='kinship',
        ),
        migrations.DeleteModel(
            name='Kinship',
        ),
    ]
