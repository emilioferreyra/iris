# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_member_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.ForeignKey(to='commons.MaritalStatus'),
        ),
    ]
