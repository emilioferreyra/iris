# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0004_auto_20160203_1243'),
        ('members', '0006_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='academic_level',
            field=models.ForeignKey(to='commons.AcademicLevel', null=True),
        ),
    ]
