# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_memberadditionalfield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cane',
            old_name='cane_number',
            new_name='name',
        ),
    ]
