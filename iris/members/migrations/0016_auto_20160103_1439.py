# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_memberaddress_address_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberaddress',
            name='province_name',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'region_name', to='location.Province', chained_field=b'region_name'),
        ),
        migrations.AlterField(
            model_name='memberaddress',
            name='town_name',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'province_name', to='location.Town', chained_field=b'province_name'),
        ),
    ]
