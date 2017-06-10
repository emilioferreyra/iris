# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0021_person_main_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='main_location',
            field=models.ForeignKey(verbose_name='Localidad', to='location.Location', null=True),
        ),
    ]
