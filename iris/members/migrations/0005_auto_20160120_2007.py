# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20160120_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberadditionalfield',
            name='observations',
            field=models.TextField(null=True, blank=True),
        ),
    ]
