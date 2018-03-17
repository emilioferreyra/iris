# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0015_auto_20170609_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaddress',
            name='address_type',
            field=models.ForeignKey(default=1, verbose_name='tipo direcci\xf3n', to='location.AddressType', help_text='Seleccione tipo de direcci\xf3n'),
        ),
    ]
