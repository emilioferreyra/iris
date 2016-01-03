# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0011_auto_20160103_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='document_type',
            field=models.ForeignKey(to='commons.DocumentType'),
        ),
    ]
