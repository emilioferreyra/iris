# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_auto_20170708_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occupation',
            options={'ordering': ['id'], 'verbose_name': 'Ocupaci\xf3n', 'verbose_name_plural': 'Ocupaciones'},
        ),
        migrations.AlterModelOptions(
            name='workplace',
            options={'ordering': ['id'], 'verbose_name': 'Lugar de trabajo', 'verbose_name_plural': 'Lugares de trabajo'},
        ),
        migrations.AlterField(
            model_name='member',
            name='where_work',
            field=models.ForeignKey(verbose_name='Lugar donde trabaja', to='members.WorkPlace', null=True),
        ),
    ]
