# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20160120_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberadditionalfield',
            name='ocupation',
            field=models.ForeignKey(blank=True, to='members.Ocupation', null=True),
        ),
        migrations.AlterField(
            model_name='memberadditionalfield',
            name='where_work',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
