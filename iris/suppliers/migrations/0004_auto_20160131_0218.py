# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_auto_20160129_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suppliercompany',
            options={'ordering': ['name'], 'verbose_name': 'Supplier Company', 'verbose_name_plural': 'Supplier Companies'},
        ),
    ]
