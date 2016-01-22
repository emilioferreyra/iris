# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20160122_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='clinic',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='member',
        ),
        migrations.RemoveField(
            model_name='prescribedmedicine',
            name='appointment',
        ),
        migrations.RemoveField(
            model_name='prescribedmedicine',
            name='medicine',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='PrescribedMedicine',
        ),
    ]
