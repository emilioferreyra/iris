# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0005_auto_20170610_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliercompany',
            name='province',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='region', default=29, verbose_name='provincia', to='location.Province', chained_field='region'),
        ),
        migrations.AlterField(
            model_name='suppliercompany',
            name='town',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='province', default=203, verbose_name='municipio', to='location.Town', chained_field='province'),
        ),
    ]
