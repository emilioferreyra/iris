# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_auto_20160122_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='address',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='province',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'region', to='location.Province', chained_field=b'region'),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='town',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'province', to='location.Town', chained_field=b'province'),
        ),
    ]
