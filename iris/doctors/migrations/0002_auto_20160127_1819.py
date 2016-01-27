# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctoradditionalfield',
            old_name='clinic',
            new_name='clinics',
        ),
    ]
