# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_workplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='where_work',
            field=models.ForeignKey(verbose_name='Empresa o lugar donde trabaja', to='members.WorkPlace', null=True),
        ),
    ]
