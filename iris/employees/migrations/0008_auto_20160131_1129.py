# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_auto_20160131_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='position_level',
            field=models.ForeignKey(to='employees.PostionLevel', null=True),
        ),
        migrations.AddField(
            model_name='postionlevel',
            name='description',
            field=models.CharField(max_length=45, unique=True, null=True),
        ),
    ]
