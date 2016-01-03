# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0012_auto_20160103_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='document_id',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='nationality',
            field=models.ForeignKey(to='location.Nationality'),
        ),
    ]
