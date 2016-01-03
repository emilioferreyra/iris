# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20160103_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='property_type',
        ),
        migrations.DeleteModel(
            name='PropertyType',
        ),
    ]
