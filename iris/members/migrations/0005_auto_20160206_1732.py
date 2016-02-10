# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20160205_1623'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='house',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='house',
            name='house_material',
        ),
        migrations.RemoveField(
            model_name='house',
            name='house_part',
        ),
        migrations.RemoveField(
            model_name='house',
            name='member_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='property_type',
        ),
        migrations.DeleteModel(
            name='House',
        ),
    ]
