# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_auto_20160124_1429'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='suppliercompany',
            table='suppliers_supplier_company',
        ),
    ]
