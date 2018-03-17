# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ocupation',
            new_name='Occupation',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='ocupation',
            new_name='occupation',
        ),
    ]
