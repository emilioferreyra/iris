# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0007_maritalstatus'),
        ('members', '0004_auto_20160103_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='marital_status',
            field=models.ForeignKey(to='commons.MaritalStatus', null=True),
        ),
    ]
