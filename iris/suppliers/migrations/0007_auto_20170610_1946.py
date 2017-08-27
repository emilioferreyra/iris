# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0006_auto_20170610_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliercontact',
            name='department',
            field=models.CharField(max_length=100, null=True, verbose_name='departamento', blank=True),
        ),
        migrations.AlterField(
            model_name='suppliercontact',
            name='extension_number',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='extensi\xf3n', blank=True),
        ),
        migrations.AlterField(
            model_name='suppliercontact',
            name='position',
            field=models.CharField(max_length=100, null=True, verbose_name='posici\xf3n', blank=True),
        ),
    ]
