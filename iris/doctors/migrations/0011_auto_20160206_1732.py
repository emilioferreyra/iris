# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0010_auto_20160205_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 6, 21, 32, 31, 323000, tzinfo=utc)),
        ),
    ]
