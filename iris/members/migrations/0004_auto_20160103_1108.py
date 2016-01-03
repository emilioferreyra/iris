# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20160103_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='marital_status',
        ),
        migrations.DeleteModel(
            name='MaritalStatus',
        ),
    ]
