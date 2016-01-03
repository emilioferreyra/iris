# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_kinsman_kinship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kinsman',
            name='kinship',
            field=models.ForeignKey(to='commons.Kinship'),
        ),
    ]
