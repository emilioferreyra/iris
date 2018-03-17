# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20160403_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='ceiling',
            new_name='ceilling',
        ),
    ]
