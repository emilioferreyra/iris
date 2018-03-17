# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_auto_20170609_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': 'WorkPlace',
                'verbose_name_plural': 'WorkPlaces',
            },
        ),
    ]
