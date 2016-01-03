# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20160103_1113'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='housematerial',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='housematerial',
            name='house_part',
        ),
        migrations.AlterUniqueTogether(
            name='housing',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='housing',
            name='house_material',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='house_part',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='member',
        ),
        migrations.DeleteModel(
            name='HouseMaterial',
        ),
        migrations.DeleteModel(
            name='HousePart',
        ),
        migrations.DeleteModel(
            name='Housing',
        ),
    ]
