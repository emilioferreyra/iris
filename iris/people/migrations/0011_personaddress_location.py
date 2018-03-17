# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20160625_1557'),
        ('people', '0010_auto_20160625_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaddress',
            name='Location',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field='town', chained_field='town', verbose_name='localidad', to='location.Location', help_text='Seleccione Localidad', null=True),
        ),
    ]
