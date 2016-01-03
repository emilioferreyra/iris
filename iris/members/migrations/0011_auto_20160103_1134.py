# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_member_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='property_type',
            field=models.ForeignKey(to='housing.PropertyType'),
        ),
    ]
