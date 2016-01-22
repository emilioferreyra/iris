# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0010_auto_20160122_1624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prescribedmedicine',
            options={'verbose_name': 'Prescribed Medicine', 'verbose_name_plural': 'Prescribed Medicines'},
        ),
        migrations.AddField(
            model_name='appointment',
            name='prescription',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_next_appoitment',
            field=models.DateField(null=True, blank=True),
        ),
    ]
