# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0012_auto_20160206_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 10, 1, 20, 1, 86551, tzinfo=utc)),
        ),
    ]
