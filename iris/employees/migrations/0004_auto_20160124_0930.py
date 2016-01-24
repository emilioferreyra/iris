# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20160122_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workday',
            options={'ordering': ['id'], 'verbose_name': 'Workday', 'verbose_name_plural': 'Workdays'},
        ),
    ]
