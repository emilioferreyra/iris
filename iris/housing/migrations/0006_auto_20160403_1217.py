# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0005_auto_20160215_2326'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HouseMaterialCeilling',
        ),
        migrations.CreateModel(
            name='HouseMaterialCeiling',
            fields=[
            ],
            options={
                'verbose_name': 'House Material Ceiling',
                'proxy': True,
                'verbose_name_plural': 'House Material Ceilings',
            },
            bases=('housing.housematerial',),
        ),
    ]
