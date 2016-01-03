# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documenttype',
            options={'verbose_name': 'Document Type', 'verbose_name_plural': 'Document Types'},
        ),
        migrations.AlterModelTable(
            name='documenttype',
            table='commons_document_type',
        ),
        migrations.AlterModelTable(
            name='phonetype',
            table='commons_phone_type',
        ),
    ]
