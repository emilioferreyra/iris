# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_auto_20160205_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='appointment_date',
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together=set([('member', 'doctor', 'appointment_date')]),
        ),
    ]
