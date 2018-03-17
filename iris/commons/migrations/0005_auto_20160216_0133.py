# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0004_auto_20160203_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academiclevel',
            old_name='academic_level',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='documenttype',
            old_name='document_type',
            new_name='name',
        ),
    ]
