# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0014_auto_20170608_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaddress',
            name='province',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='region', default=29, verbose_name='provincia', to='location.Province', chained_field='region', help_text='Seleccione provincia'),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='region',
            field=models.ForeignKey(default=1, verbose_name='regi\xf3n', to='location.Region', help_text='Seleccione regi\xf3n'),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='town',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='province', default=203, verbose_name='municipio', to='location.Town', chained_field='province', help_text='Seleccione municipio'),
        ),
    ]
