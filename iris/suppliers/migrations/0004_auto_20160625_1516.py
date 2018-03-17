# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_suppliercontact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suppliercontact',
            name='movil_number',
        ),
        migrations.AddField(
            model_name='suppliercontact',
            name='mobile_number',
            field=localflavor.us.models.PhoneNumberField(max_length=20, null=True, verbose_name='tel\xe9fono m\xf3vil', blank=True),
        ),
        migrations.AlterField(
            model_name='suppliercontact',
            name='extension_number',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='n\xfamero de extensi\xf3n', blank=True),
        ),
    ]
