# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0004_auto_20160215_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housematerial',
            name='house_part',
            field=models.ForeignKey(to='housing.HousePart'),
        ),
    ]
