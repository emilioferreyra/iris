# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0015_auto_20160103_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='active',
        ),
    ]
