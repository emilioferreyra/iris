# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20160203_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personphone',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(help_text='999-999-9999', max_length=20),
        ),
        migrations.AlterField(
            model_name='personphone',
            name='phone_type',
            field=models.ForeignKey(to='commons.PhoneType'),
        ),
    ]
