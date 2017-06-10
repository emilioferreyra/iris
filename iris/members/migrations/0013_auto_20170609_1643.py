# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_member_children_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='children_quantity',
            field=models.PositiveIntegerField(null=True, verbose_name='Cantidad de hijos'),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_mother',
            field=models.BooleanField(default=False, verbose_name='Es madre'),
        ),
    ]
