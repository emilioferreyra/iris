# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0007_maritalstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kinship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kinship', models.CharField(unique=True, max_length=45)),
            ],
        ),
    ]
