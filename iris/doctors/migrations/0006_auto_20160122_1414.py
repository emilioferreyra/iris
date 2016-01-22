# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20160120_1658'),
        ('doctors', '0005_auto_20160122_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='province_name',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='town_name',
        ),
        migrations.AddField(
            model_name='clinic',
            name='province',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'region', default=29, to='location.Province', chained_field=b'region'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='town',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'province', default=203, to='location.Town', chained_field=b'province'),
        ),
    ]
