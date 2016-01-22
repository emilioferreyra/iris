# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0008_auto_20160122_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctoradditionalfield',
            name='clinic',
        ),
        migrations.AddField(
            model_name='doctoradditionalfield',
            name='clinic',
            field=models.ManyToManyField(to='doctors.Clinic'),
        ),
    ]
