# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dependent_of',
            field=models.ForeignKey(verbose_name='supervisor', blank=True, to='people.Person', null=True),
        ),
    ]
