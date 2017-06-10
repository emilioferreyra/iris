# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20170608_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addresstype',
            options={'ordering': ['id'], 'verbose_name': 'Tipo de direcci\xf3n', 'verbose_name_plural': 'Tipo de direcciones'},
        ),
    ]
