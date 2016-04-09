# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_housematerialceilling_housematerialfloor_housematerialwall'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='housematerial',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='housematerial',
            name='house_part',
        ),
        migrations.DeleteModel(
            name='HousePart',
        ),
    ]
