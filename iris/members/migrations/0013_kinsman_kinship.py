# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0008_kinship'),
        ('members', '0012_auto_20160103_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='kinsman',
            name='kinship',
            field=models.ForeignKey(to='commons.Kinship', null=True),
        ),
    ]
