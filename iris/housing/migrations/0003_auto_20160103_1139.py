# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_propertytype'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='housematerial',
            table='housing_house_material',
        ),
        migrations.AlterModelTable(
            name='housepart',
            table='housing_house_part',
        ),
        migrations.AlterModelTable(
            name='propertytype',
            table='housing_property_type',
        ),
    ]
