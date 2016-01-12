# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0003_auto_20160112_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonetype',
            old_name='phone_type',
            new_name='name',
        ),
    ]
