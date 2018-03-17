# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_auto_20160625_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_day',
            field=models.DateField(help_text='Introduzca Fecha de nacimiento', null=True, verbose_name='Fecha nacimiento', blank=True),
        ),
    ]
