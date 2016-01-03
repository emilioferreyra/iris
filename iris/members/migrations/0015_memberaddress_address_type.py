# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_addresstype'),
        ('members', '0014_auto_20160103_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberaddress',
            name='address_type',
            field=models.ForeignKey(to='location.AddressType', null=True),
        ),
    ]
