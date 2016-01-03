# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='academic_level',
            field=models.ForeignKey(to='commons.AcademicLevel'),
        ),
        migrations.DeleteModel(
            name='AcademicLevel',
        ),
    ]
