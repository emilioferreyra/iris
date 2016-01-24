# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_persontype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persontype',
            options={'ordering': ['id'], 'verbose_name': 'Person Type', 'verbose_name_plural': 'Person Types'},
        ),
        migrations.AlterField(
            model_name='person',
            name='person_type',
            field=models.ForeignKey(to='people.PersonType', null=True),
        ),
    ]
