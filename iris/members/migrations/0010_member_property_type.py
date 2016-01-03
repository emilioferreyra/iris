# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_propertytype'),
        ('members', '0009_auto_20160103_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='property_type',
            field=models.ForeignKey(to='housing.PropertyType', null=True),
        ),
    ]
