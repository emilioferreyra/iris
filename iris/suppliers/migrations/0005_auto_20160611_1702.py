# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0004_auto_20160131_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliertype',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
    ]
