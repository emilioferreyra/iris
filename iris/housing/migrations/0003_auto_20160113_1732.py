# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_auto_20160112_0016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='housematerial',
            options={'ordering': ['id']},
        ),
    ]
