# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20160203_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_number',
            field=models.IntegerField(null=True),
        ),
    ]
