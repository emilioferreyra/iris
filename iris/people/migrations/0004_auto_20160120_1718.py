# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20160120_1658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['id'], 'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
    ]
