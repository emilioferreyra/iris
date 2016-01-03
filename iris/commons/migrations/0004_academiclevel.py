# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0003_remove_contactinfo_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_level', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'db_table': 'members_academic_level',
            },
        ),
    ]
