# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0022_auto_20170610_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='main_location',
            field=models.ForeignKey(verbose_name='Localidad', blank=True, to='location.Location', null=True),
        ),
    ]
