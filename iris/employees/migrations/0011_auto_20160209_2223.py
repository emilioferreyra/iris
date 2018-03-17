# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_employee_academic_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='academic_level',
            field=models.ForeignKey(to='commons.AcademicLevel'),
        ),
    ]
