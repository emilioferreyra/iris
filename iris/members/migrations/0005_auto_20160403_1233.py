# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20160403_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='ceilling',
            new_name='ceiling',
        ),
    ]
