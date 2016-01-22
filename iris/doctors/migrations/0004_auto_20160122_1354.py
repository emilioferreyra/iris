# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20160120_1658'),
        ('doctors', '0003_auto_20160121_1933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clinic',
            options={'ordering': ['name'], 'verbose_name': 'Clinic', 'verbose_name_plural': 'Clinics'},
        ),
        migrations.AddField(
            model_name='clinic',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(help_text=b'999-999-9999', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='province_name',
            field=models.ForeignKey(to='location.Province', null=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='region',
            field=models.ForeignKey(to='location.Region', null=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='town_name',
            field=models.ForeignKey(to='location.Town', null=True),
        ),
    ]
