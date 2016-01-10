# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20160110_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kinsman',
            fields=[
            ],
            options={
                'verbose_name': 'Kinsman',
                'proxy': True,
                'verbose_name_plural': 'Kinsmans',
            },
            bases=('people.person',),
        ),
    ]
