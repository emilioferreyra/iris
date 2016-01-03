# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0016_remove_contactinfo_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
