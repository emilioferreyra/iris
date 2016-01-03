# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_material', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'members_house_material',
            },
        ),
        migrations.CreateModel(
            name='HousePart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_part', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='housematerial',
            name='house_part',
            field=models.ForeignKey(to='housing.HousePart'),
        ),
        migrations.AlterUniqueTogether(
            name='housematerial',
            unique_together=set([('house_material', 'house_part')]),
        ),
    ]
