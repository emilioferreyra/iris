# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseMaterialCeilling',
            fields=[
            ],
            options={
                'verbose_name': 'HouseMaterialCeilling',
                'proxy': True,
                'verbose_name_plural': 'HouseMaterialCeillings',
            },
            bases=('housing.housematerial',),
        ),
        migrations.CreateModel(
            name='HouseMaterialFloor',
            fields=[
            ],
            options={
                'verbose_name': 'HouseMaterialFloor',
                'proxy': True,
                'verbose_name_plural': 'HouseMaterialFloors',
            },
            bases=('housing.housematerial',),
        ),
        migrations.CreateModel(
            name='HouseMaterialWall',
            fields=[
            ],
            options={
                'verbose_name': 'HouseMaterialWall',
                'proxy': True,
                'verbose_name_plural': 'HouseMaterialWalls',
            },
            bases=('housing.housematerial',),
        ),
    ]
