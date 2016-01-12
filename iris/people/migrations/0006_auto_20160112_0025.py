# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_remove_person_dependent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mother_last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='nationality',
            field=models.ForeignKey(default=1, to='location.Nationality'),
        ),
    ]
