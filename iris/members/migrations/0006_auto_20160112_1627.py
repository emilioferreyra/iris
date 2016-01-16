# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20160112_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memberadditionalfield',
            options={'verbose_name': 'Additional Field', 'verbose_name_plural': 'Additional Fields'},
        ),
    ]
