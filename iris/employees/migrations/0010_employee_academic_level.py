# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0004_auto_20160203_1243'),
        ('employees', '0009_auto_20160131_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='academic_level',
            field=models.ForeignKey(to='commons.AcademicLevel', null=True),
        ),
    ]
