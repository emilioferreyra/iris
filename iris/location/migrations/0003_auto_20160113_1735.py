# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_province_town'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nationality',
            options={'ordering': ['name'], 'verbose_name': 'Nationality', 'verbose_name_plural': 'Nationalities'},
        ),
    ]
