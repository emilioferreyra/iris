# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_member_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_number',
            field=models.IntegerField(default=members.models.number, unique=True),
        ),
    ]
