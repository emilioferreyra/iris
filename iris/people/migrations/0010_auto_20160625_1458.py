# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20160611_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='people_pictures', blank=True),
        ),
    ]
