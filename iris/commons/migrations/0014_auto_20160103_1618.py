# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0013_auto_20160103_1550'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AcademicLevel',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='document_type',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='nationality',
        ),
        migrations.DeleteModel(
            name='Kinship',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='phone_type',
        ),
        migrations.DeleteModel(
            name='ContactInfo',
        ),
        migrations.DeleteModel(
            name='DocumentType',
        ),
        migrations.DeleteModel(
            name='MaritalStatus',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.DeleteModel(
            name='PhoneType',
        ),
    ]
