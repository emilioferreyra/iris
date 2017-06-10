# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0013_auto_20170608_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='marital_status',
            field=models.ForeignKey(blank=True, to='commons.MaritalStatus', help_text='Seleccione estado civil', null=True, verbose_name='estado civil'),
        ),
    ]
