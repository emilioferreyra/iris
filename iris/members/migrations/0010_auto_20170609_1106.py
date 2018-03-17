# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_auto_20170609_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='occupation',
            field=models.ManyToManyField(help_text='Seleccione ocupaci\xf3n', to='members.Occupation', verbose_name='Ocupaci\xf3n(es)'),
        ),
    ]
