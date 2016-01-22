# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_auto_20160122_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='address',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(help_text=b'999-999-9999', max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='province_name',
            field=models.ForeignKey(default=29, to='location.Province', null=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='region',
            field=models.ForeignKey(default=1, to='location.Region', null=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='town_name',
            field=models.ForeignKey(default=203, to='location.Town', null=True),
        ),
    ]
