# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kinship',
            old_name='kinship',
            new_name='name',
        ),
    ]
