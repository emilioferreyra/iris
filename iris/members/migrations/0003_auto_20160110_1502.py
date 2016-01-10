# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_delete_memberkinsman'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cane',
            old_name='cane',
            new_name='cane_number',
        ),
    ]
