# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='housematerial',
            old_name='house_material',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='housepart',
            old_name='house_part',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='propertytype',
            old_name='property_type',
            new_name='name',
        ),
        migrations.AlterUniqueTogether(
            name='housematerial',
            unique_together=set([('name', 'house_part')]),
        ),
    ]
