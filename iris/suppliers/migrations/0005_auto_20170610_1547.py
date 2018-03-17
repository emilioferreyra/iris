# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0004_auto_20160625_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliercontact',
            name='department',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='suppliercontact',
            name='position',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
