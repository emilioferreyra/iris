# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0002_auto_20160110_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maritalstatus',
            old_name='marital_status',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(help_text=b'999-999-9999', max_length=20),
        ),
    ]
