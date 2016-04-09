# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0003_auto_20160215_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='HousePart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'housing_house_part',
            },
        ),
        migrations.AlterModelOptions(
            name='housematerialceilling',
            options={'verbose_name': 'House Material Ceilling', 'verbose_name_plural': 'House Material Ceillings'},
        ),
        migrations.AlterModelOptions(
            name='housematerialfloor',
            options={'verbose_name': 'House Material  Floor', 'verbose_name_plural': 'House Material Floors'},
        ),
        migrations.AlterModelOptions(
            name='housematerialwall',
            options={'verbose_name': 'House Material Wall', 'verbose_name_plural': 'House Material Walls'},
        ),
        migrations.AddField(
            model_name='housematerial',
            name='house_part',
            field=models.ForeignKey(to='housing.HousePart', null=True),
        ),
    ]
