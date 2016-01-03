# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0005_auto_20160102_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='phone_type',
        ),
        migrations.AlterModelOptions(
            name='documenttype',
            options={'verbose_name': 'Document Type', 'verbose_name_plural': 'Documents types'},
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]
