# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name'], 'verbose_name': 'Pa\xeds', 'verbose_name_plural': 'Paices'},
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(unique=True, max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='nationality',
            name='name',
            field=models.CharField(unique=True, max_length=30, verbose_name='nombre'),
        ),
    ]
