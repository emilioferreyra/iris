# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20160625_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name'], 'verbose_name': 'Pa\xeds', 'verbose_name_plural': 'Paises'},
        ),
    ]
