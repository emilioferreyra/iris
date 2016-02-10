# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_housematerialceilling_housematerialfloor_housematerialwall'),
        ('members', '0005_auto_20160206_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ceilling', models.ForeignKey(to='housing.HouseMaterialCeilling')),
                ('floor', models.ForeignKey(to='housing.HouseMaterialFloor')),
                ('member_name', models.ForeignKey(to='members.Member')),
                ('property_type', models.ForeignKey(to='housing.PropertyType')),
                ('wall', models.ForeignKey(to='housing.HouseMaterialWall')),
            ],
        ),
    ]
