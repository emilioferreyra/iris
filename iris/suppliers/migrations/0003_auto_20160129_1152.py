# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_auto_20160129_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliercompany',
            name='region',
            field=models.ForeignKey(default=1, to='location.Region'),
        ),
    ]
