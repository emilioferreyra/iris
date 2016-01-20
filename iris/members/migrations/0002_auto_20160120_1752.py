# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberadditionalfield',
            name='currently_works',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='memberadditionalfield',
            name='ocupation',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='memberadditionalfield',
            name='where_work',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Where you Work'),
        ),
    ]
