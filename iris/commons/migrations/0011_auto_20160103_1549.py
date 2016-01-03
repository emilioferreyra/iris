# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0010_auto_20160103_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='marital_status',
            field=models.ForeignKey(to='commons.MaritalStatus'),
        ),
    ]
