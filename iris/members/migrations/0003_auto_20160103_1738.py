# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20160103_1715'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MemberPhones',
            new_name='MemberPhone',
        ),
    ]
