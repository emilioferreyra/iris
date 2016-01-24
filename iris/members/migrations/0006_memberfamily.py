# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20160124_1036'),
        ('members', '0005_auto_20160120_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberFamily',
            fields=[
            ],
            options={
                'verbose_name': 'Member Family',
                'proxy': True,
                'verbose_name_plural': 'Member Families',
            },
            bases=('people.person',),
        ),
    ]
