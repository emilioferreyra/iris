# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0004_auto_20160124_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactadditionalfield',
            old_name='supplier_name',
            new_name='supplier_company',
        ),
        migrations.AddField(
            model_name='suppliercompany',
            name='company_logo',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='suppliers_logos', blank=True),
        ),
    ]
